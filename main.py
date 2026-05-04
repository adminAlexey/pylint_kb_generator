#!/usr/bin/env python3
"""
Pylint -> Markdown KB
"""

import argparse
import html
import json
import logging
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, List, Optional, Union, cast
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = (
    "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
)
OUTPUT_BASE_DIR = Path("knowledge-base/pylint-rules")
REQUEST_TIMEOUT = 30
VERSION_MARKER_START = "<!-- PYLINT_VERSION_START -->"
VERSION_MARKER_END = "<!-- PYLINT_VERSION_END -->"
README_PATH = Path("Readme.md")


@dataclass
class PylintRule:
    rule_code: str
    rule_name: str
    category: str = "pylint"
    tags: List[str] = field(default_factory=lambda: ["python"])
    related: List[str] = field(default_factory=list)
    source: str = BASE_URL
    link: str = ""
    content_md: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)

    def to_markdown(self) -> str:
        """Generates Markdown with frontmatter"""
        rule_id = f"pylint-{self.rule_code}"

        yaml_lines = [
            "---",
            f"id: {rule_id}",
            f'rule_code: "{self.rule_code}"',
            f'rule_name: "{self.rule_name}"',
            f'category: "{self.category}"',
            'tags: ["python"]',
            "related: []",
            f'source: "{self.source}"',
            f'link: "{self.link}"',
            "---",
            "",
        ]

        return "\n".join(yaml_lines) + self.content_md


def fetch_page(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[str]:
    """Fetch webpage content with error handling"""
    try:
        logger.info("Fetching %s", url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding or "utf-8"
        return response.text
    except requests.RequestException as e:
        logger.error("Failed to fetch %s: %s", url, e)
        return None


def parse_main_page(page: str, url: str) -> List[dict]:
    """Extracts links to rules."""
    soup = BeautifulSoup(page, "html.parser")

    rules = []
    for a in soup.find_all("a", class_="reference internal", href=True):
        href = urljoin(url, str(a["href"]))
        text = a.get_text(strip=True)

        if "messages_overview" in href or "index.html" in href:
            continue

        match = re.match(r"^(.+?)\s*[/–—]\s*([A-Z]\d{3,4})$", text)
        if not match:
            match = re.match(r"^([A-Z]\d{3,4})\s*[/–—]\s*(.+?)$", text)

        if match:
            part1, part2 = match.group(1).strip(), match.group(2).strip()
            if re.match(r"^[A-Z]\d{3,4}$", part1):
                rule_code, rule_name = part1, part2
            else:
                rule_name, rule_code = part1, part2

            rule_name = re.sub(
                r"[^a-z0-9_\-.]", "", rule_name.lower().replace(" ", "-")
            )

            rules.append(
                {
                    "rule_code": rule_code,
                    "rule_name": rule_name,
                    "href": href,
                    "text": text,
                }
            )

    return rules


def parse_rule_page(href: str) -> dict:
    """Converts the rules page to Markdown"""
    result = {"content_md": ""}

    content = fetch_page(href)
    if not content:
        return result

    soup = BeautifulSoup(content, "html.parser")

    main_section = soup.find("section")
    if not main_section:
        main_section = soup.find("main") or soup.find("body")

    if main_section:
        md_content = html_to_markdown(main_section, BASE_URL)
        md_content = re.sub(r"\n{3,}", "\n\n", md_content)
        result["content_md"] = md_content.strip()

    return result


def _handle_text(element: NavigableString) -> str:
    """Handle plain text nodes."""
    return html.unescape(str(element))


def _handle_heading(element: Tag, _base_url: str) -> str:
    """Handle h1-h6 tags."""
    level = int(element.name[1])
    # Remove headerlink anchors
    for anchor in element.find_all("a", class_="headerlink"):
        anchor.decompose()
    text = element.get_text(strip=True)
    return f"\n{'#' * level} {text}\n\n"


def _handle_paragraph(element: Tag, base_url: str) -> str:
    """Handle <p> tags."""
    inner = "".join(
        html_to_markdown(cast(Union[Tag, NavigableString], child), base_url)
        for child in element.children
    )
    inner = inner.strip()
    return f"{inner}\n\n" if inner else ""


def _handle_code_block(element: Tag, _base_url: str) -> str:
    """Handle <pre> blocks with optional <code> child."""
    code = element.find("code")
    if code:
        raw_classes = code.get("class")
        # Type narrowing for BS4 class attribute
        if isinstance(raw_classes, str):
            classes = [raw_classes]
        elif raw_classes:
            classes = list(raw_classes)
        else:
            classes = []
        lang = "python" if any("python" in c for c in classes) else ""
        code_text = code.get_text()
    else:
        lang = ""
        code_text = element.get_text()
    return f"\n```{lang}\n{code_text.strip()}\n```\n\n"


def _handle_list(element: Tag, base_url: str) -> str:
    """Handle <ul> and <ol> lists."""
    items = []
    for i, li in enumerate(element.find_all("li", recursive=False), 1):
        inner = html_to_markdown(li, base_url).strip()
        prefix = "- " if element.name == "ul" else f"{i}. "
        items.append(f"{prefix}{inner}")
    return "\n" + "\n".join(items) + "\n\n"


def _handle_table(element: Tag, _base_url: str) -> str:
    """Handle <table> tags."""
    rows = []
    for tr in element.find_all("tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        if cells:
            rows.append("| " + " | ".join(cells) + " |")
    if not rows:
        return ""
    separator = "| " + " | ".join(["---"] * len(rows[0].split("|")[1:-1])) + " |"
    result = [rows[0], separator] + rows[1:]
    return "\n" + "\n".join(result) + "\n\n"


def _handle_definition_list(element: Tag, _base_url: str) -> str:
    """Handle <dl> definition lists."""
    parts = []
    for dt in element.find_all("dt"):
        term = dt.get_text(strip=True)
        dd = dt.find_next_sibling("dd")
        desc = dd.get_text(strip=True) if dd else ""
        parts.append(f"**{term}**\n: {desc}")
    return "\n".join(parts) + "\n\n"


def _handle_horizontal_rule(_element: Tag, _base_url: str) -> str:
    """Handle <hr> tags."""
    return "\n---\n\n"


def _handle_blockquote(element: Tag, base_url: str) -> str:
    """Handle <blockquote> tags."""
    inner = "".join(
        html_to_markdown(cast(Union[Tag, NavigableString], c), base_url)
        for c in element.children
    )
    quoted = "\n".join(f"> {line}" for line in inner.strip().split("\n"))
    return f"\n{quoted}\n\n"


def _handle_inline_formatting(element: Tag, base_url: str) -> str:
    """Handle <strong>, <b>, <em>, <i> tags."""
    tag_name = element.name.lower()
    wrapper = "**" if tag_name in ("strong", "b") else "*"
    inner = "".join(
        html_to_markdown(cast(Union[Tag, NavigableString], c), base_url)
        for c in element.children
    )
    return f"{wrapper}{inner.strip()}{wrapper}"


def _handle_inline_code(element: Tag, _base_url: str) -> str:
    """Handle inline <code> tags (not inside <pre>)."""
    if element.parent and element.parent.name == "pre":
        return element.get_text()
    text = element.get_text()
    return f"`{text.strip()}`"


def _handle_span(element: Tag, base_url: str) -> str:
    """Handle <span class='pre'> tags."""
    if "pre" in (element.get("class") or []):
        return f"`{element.get_text()}`"
    # Fallback: process children
    return "".join(
        html_to_markdown(cast(Union[Tag, NavigableString], c), base_url)
        for c in element.children
    )


def _handle_link(element: Tag, base_url: str) -> str:
    """Handle <a> tags."""
    text = element.get_text(strip=True)
    href = element.get("href")
    # Type narrowing for href attribute
    if not isinstance(href, str) or not href or href.startswith("#"):
        return text
    if base_url and not href.startswith("https://"):
        href = urljoin(base_url, href)
    return f"[{text}]({href})"


def _handle_image(element: Tag, _base_url: str) -> str:
    """Handle <img> tags."""
    alt = element.get("alt", "image")
    src = element.get("src", "")
    return f"![{alt}]({src})"


def _handle_line_break(_element: Tag, _base_url: str) -> str:
    """Handle <br> tags."""
    return "  \n"


def _handle_skip(_element: Tag, _base_url: str) -> str:
    """Handle tags that should be skipped (script, style, etc.)."""
    return ""


def _has_headerlink_class(element: Tag) -> bool:
    """Check if element has 'headerlink' class (type-safe)."""
    classes = element.get("class")
    if isinstance(classes, str):
        return "headerlink" in classes
    if classes:
        return "headerlink" in classes
    return False


# Dispatch table: tag name -> handler function
_TAG_HANDLERS: dict[str, Callable[[Tag, str], str]] = {
    # Block elements
    "h1": _handle_heading,
    "h2": _handle_heading,
    "h3": _handle_heading,
    "h4": _handle_heading,
    "h5": _handle_heading,
    "h6": _handle_heading,
    "p": _handle_paragraph,
    "pre": _handle_code_block,
    "ul": _handle_list,
    "ol": _handle_list,
    "table": _handle_table,
    "dl": _handle_definition_list,
    "hr": _handle_horizontal_rule,
    "blockquote": _handle_blockquote,
    # Inline formatting
    "strong": _handle_inline_formatting,
    "b": _handle_inline_formatting,
    "em": _handle_inline_formatting,
    "i": _handle_inline_formatting,
    "code": _handle_inline_code,
    "span": _handle_span,
    "a": _handle_link,
    "img": _handle_image,
    "br": _handle_line_break,
    # Skip these tags
    "script": _handle_skip,
    "style": _handle_skip,
    "nav": _handle_skip,
    "footer": _handle_skip,
    "header": _handle_skip,
}


def html_to_markdown(element: Union[Tag, NavigableString], base_url: str = "") -> str:
    """
    Recursively convert HTML element to Markdown.
    Supports: headings, code, lists, tables, links, inline formatting.
    """
    # Base case: text node
    if isinstance(element, NavigableString):
        return _handle_text(element)

    tag_name = element.name.lower() if element.name else ""

    # Skip headerlink anchors
    if _has_headerlink_class(element):
        return ""

    # Dispatch to handler or fallback to recursive children processing
    handler = _TAG_HANDLERS.get(tag_name)
    if handler:
        return handler(element, base_url)

    # Fallback: process children recursively
    return "".join(
        html_to_markdown(cast(Union[Tag, NavigableString], child), base_url)
        for child in element.children
    )


def get_pylint_version(url) -> Optional[str]:
    """Extract Pylint version from the main documentation page."""
    page = fetch_page(url)
    if not page:
        return None
    soup = BeautifulSoup(page, "html.parser")
    # Try to find version in the title like "Pylint 3.3.1 documentation"
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.get_text(strip=True)
        match = re.search(r"Pylint\s+([\d.]+)", title_text)
        if match:
            return match.group(1)
    # Fallback: look for a span with class 'version'
    version_span = soup.find("span", class_="sidebar-brand-text")
    if version_span:
        return version_span.get_text(strip=True)
    return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Pylint Messages Parser -> Markdown KB (full content)"
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        default=BASE_URL,
        help="URL to pylint rules documentation",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=str(OUTPUT_BASE_DIR),
        help="Base directory for output",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument(
        "--dry-run", action="store_true", help="Parse but don't save files"
    )

    args = parser.parse_args()

    page = fetch_page(args.url)
    if not page:
        logger.error("Failed to fetch documentation page")
        return 1

    # Updating the markdown pylint version
    version_str = get_pylint_version(BASE_URL)
    content = README_PATH.read_text(encoding="utf-8")
    new_content = re.sub(
        f"{re.escape(VERSION_MARKER_START)}.*?{re.escape(VERSION_MARKER_END)}",
        f"{VERSION_MARKER_START} Pylint v{version_str} {VERSION_MARKER_END}",
        content,
        flags=re.DOTALL,
    )
    README_PATH.write_text(new_content, encoding="utf-8")

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    rule_links = parse_main_page(page, args.url)
    logger.info("🔗 Rules found: %d", len(rule_links))

    rules: List[PylintRule] = []

    for item in tqdm(rule_links):
        details = parse_rule_page(href=item["href"])

        rule = PylintRule(
            rule_code=item["rule_code"],
            rule_name=item["rule_name"],
            link=item["href"],
            content_md=details.get("content_md", "⚠️ The content is not extracted."),
        )
        rules.append(rule)
        logger.info(
            "   📝 %s — %s (%d characters.)",
            item["rule_code"],
            item["rule_name"],
            len(details.get("content_md", "")),
        )

    if args.dry_run:
        logger.info("\n📋 An example of a card (the first 1500 characters):")
        logger.info(rules[0].to_markdown()[:1500] + "\n...")
        sys.exit(0)

    saved = skipped = 0
    for rule in rules:
        filename = f"{rule.rule_code.lower()}-{rule.rule_name}.md"
        filepath = output_dir / filename

        if filepath.exists() and not args.force:
            skipped += 1
            continue

        filepath.write_text(rule.to_markdown(), encoding="utf-8")
        saved += 1

    index_path = output_dir / "pylint_index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump([r.to_dict() for r in rules], f, ensure_ascii=False, indent=2)

    logger.info("\n📊 Index: %s", index_path)
    logger.info("✨ Done: %d saved, %d skipped", saved, skipped)

    return 0


if __name__ == "__main__":
    main()
