# Pylint KB Generator

### <!-- PYLINT_VERSION_START --> Pylint v4.1.0 <!-- PYLINT_VERSION_END -->

Automatically transforms Pylint's official documentation into clean, structured Markdown cards tailored for **Retrieval-Augmented Generation (RAG)** pipelines. 

Instead of manually curating linting rules or scraping outdated HTML, this tool fetches the latest documentation directly from ReadTheDocs, parses it into a consistent format, and outputs ready-to-index files alongside a JSON manifest.

### 🔍 Why it exists
LLM-powered code assistants and static analysis bots need accurate, up-to-date linting rules. `pylint-kb-parser` bridges the gap between Pylint's evolving documentation and static RAG knowledge bases, ensuring your AI tools always reference the correct rule behavior, examples, and auto-fix commands.

### ✨ Key Features
- **Live fetching**: No local HTML dumps required. Parses directly from the web.
- **RAG-optimized output**: Consistent frontmatter, clean Markdown, and a machine-readable `pylint_index.json`.
- **Fast & polite**: Parallel HTTP requests with built-in rate limiting and `tqdm` progress tracking.
- **Configurable**: `pyproject.toml` defaults with full CLI override support for CI/CD pipelines.
- **Modern Python**: Type-safe, `dataclass`-driven, and dispatch-based HTML→Markdown conversion.

### 🚀 Quick Start

Installation

```bash
uv sync
```

Run the application

```bash
uv run main.py
```

### ⚙️ CLI Options
| Flag | Description | Default                                                                              |
|------|-------------|--------------------------------------------------------------------------------------|
| `-u, --url` | Documentation URL | `https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html` |
| `-o, --output` | Output directory | `knowledge-base/pylint-rules`                                                        |
| `-f, --force` | Overwrite existing files | `False`                                                                              |
| `--dry-run` | Parse without saving | `False`                                                                              |