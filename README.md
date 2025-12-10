<div align="center">
  <img src="https://assets.website-files.com/624ea00c0a0c641ac82b9933/62e3d3600f90e5f98887ee23_logo-webflow.svg" alt="TorrentScout Logo" width="150" height="150">
  <h1>TorrentScout-qBittorrent-Search-Plugin-Suite</h1>
</div>

<div align="center">
  <p>
    <a href="https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/actions/workflows/ci.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/ci.yml?branch=main&style=flat-square&label=Build%20Status" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite">
      <img src="https://img.shields.io/codecov/c/github/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite?style=flat-square&token=YOUR_CODECOV_TOKEN" alt="Code Coverage">
    </a>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/qBittorrent-4.x%2B-green?style=flat-square&logo=qbittorrent&logoColor=white" alt="qBittorrent Version">
    <img src="https://img.shields.io/badge/Linter-Ruff-black?style=flat-square&logo=ruff" alt="Ruff Linter">
    <a href="https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square" alt="License">
    </a>
    <a href="https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/stargazers">
      <img src="https://img.shields.io/github/stars/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite?style=flat-square&color=yellow" alt="GitHub Stars">
    </a>
  </p>
  <p>
    <a href="https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/stargazers">
      <img src="https://img.shields.io/static/v1?label=Star%20⭐%20this%20Repo&message=if%20you%20find%20it%20useful&color=brightgreen&style=flat-square" alt="Star this Repo">
    </a>
  </p>
</div>

A high-performance Python-based search plugin suite for qBittorrent, TorrentScout seamlessly integrates with popular torrent search engines to provide an enhanced and efficient content discovery experience directly within your favorite torrent client. This project empowers users with robust automation capabilities, efficient web scraping, and a flexible architecture for extended functionality.

## 🚀 Key Features

*   **Seamless qBittorrent Integration:** Directly extend qBittorrent's search capabilities.
*   **Modular Plugin Architecture:** Easily add or modify search providers.
*   **High-Performance Web Scraping:** Optimized for speed and reliability.
*   **Automated Content Discovery:** Streamline your torrent acquisition workflow.
*   **Pythonic & Maintainable Codebase:** Built with modern Python standards, linted by Ruff, and tested with Pytest.

## 📦 Project Structure


.
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   ├── CONTRIBUTING.md
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── SECURITY.md
├── src/
│   └── torrentscout/
│       ├── __init__.py
│       ├── core/             # Core plugin logic, abstract base classes
│       │   ├── __init__.py
│       │   └── base_plugin.py
│       ├── providers/        # Individual search engine plugins
│       │   ├── __init__.py
│       │   ├── torrentz.py
│       │   └── nyaa.py
│       ├── utils/            # Utility functions (e.g., HTTP requests, parsing)
│       │   └── __init__.py
│       ├── main.py           # Main entry point for CLI or direct execution
│       └── config.py         # Configuration management
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   └── test_core.py
│   └── integration/
│       └── test_providers.py
├── .gitignore
├── AGENTS.md
├── badges.yml
├── LICENSE
├── PROPOSED_README.md
├── README.md
├── pyproject.toml
└── requirements.txt


## 📜 Table of Contents

*   [🚀 Key Features](#-key-features)
*   [📦 Project Structure](#-project-structure)
*   [📜 Table of Contents](#-table-of-contents)
*   [🛠️ Setup & Installation](#️-setup--installation)
    *   [Prerequisites](#prerequisites)
    *   [Quick Start](#quick-start)
    *   [Integrating with qBittorrent](#integrating-with-qbittorrent)
*   [⚙️ Usage](#️-usage)
*   [🧪 Testing](#-testing)
*   [CONTRIBUTING.md](#contributingmd)
*   [🛡️ Security](#️-security)
*   [🤝 Contributing](#-contributing)
*   [📄 License](#-license)
*   [🤖 AI Agent Directives](#-ai-agent-directives)
*   [udos](#udos)

## 🛠️ Setup & Installation

### Prerequisites

Ensure you have the following installed:

*   **Python 3.10+**: Download from [python.org](https://www.python.org/).
*   **qBittorrent 4.x+**: Download from [qbittorrent.org](https://www.qbittorrent.org/).
*   **`uv`**: Recommended for fast dependency management. Install with `pip install uv`.

### Quick Start

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite.git
    cd TorrentScout-qBittorrent-Search-Plugin-Suite
    

2.  **Create and activate a virtual environment (recommended):**
    bash
    uv venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    

3.  **Install dependencies:**
    bash
    uv pip install -r requirements.txt
    
    Alternatively, using pip:
    bash
    pip install -r requirements.txt
    

4.  **Run linters and tests:**
    bash
    uv run ruff check .
    uv run ruff format .
    uv run pytest
    
    Alternatively, using python directly:
    bash
    python -m ruff check .
    python -m ruff format .
    python -m pytest
    

### Integrating with qBittorrent

Detailed instructions for adding `TorrentScout` plugins to your qBittorrent instance can be found in our [Integration Guide](docs/integration.md) (or similar future doc). Typically, this involves:

1.  Opening qBittorrent.
2.  Navigating to `View > Search engine`.
3.  Clicking `Search plugins...` and then `Install a new one...`.
4.  Selecting the `.py` files from the `src/torrentscout/providers/` directory or a combined `.json` definition.

## ⚙️ Usage

After installation and integration with qBittorrent, you can use the search plugins directly from qBittorrent's "Search" tab.

To run specific plugins or test them from the command line (for development/debugging):

bash
uv run python src/torrentscout/main.py --search "your query" --provider torrentz
# Or run a specific provider directly (example, depends on provider implementation)
uv run python src/torrentscout/providers/nyaa.py "your query"


## 🧪 Testing

TorrentScout uses `pytest` for its testing suite.

To run all tests:

bash
uv run pytest


To run tests with coverage reporting:

bash
uv run pytest --cov=src/torrentscout --cov-report=term-missing


## CONTRIBUTING.md

All contributions are welcome! Please see our [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to get started, report bugs, suggest features, and submit pull requests.

## 🛡️ Security

We take security seriously. Please report any vulnerabilities responsibly by following the guidelines in our [SECURITY.md](.github/SECURITY.md) document.

## 🤝 Contributing

We welcome contributions from the community! Please refer to our [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed instructions on how to contribute.

## 📄 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International Public License](LICENSE).

---

## 🤖 AI Agent Directives

<details>
<summary><b>Expand for AI Agent Directives (CRITICAL for Automated Operations)</b></summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**. This repository, `TorrentScout-qBittorrent-Search-Plugin-Suite`, is a Python-based search plugin suite for qBittorrent.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like web scraping, plugin management, and qBittorrent integration, while maintaining a unified deployment. Focus on **Hexagonal Architecture** (Ports & Adapters) for plugin design, allowing easy swapping of search providers.
    *   **CLI Framework:** Uses `argparse` or similar for powerful and intuitive command-line interface for plugin development and testing.

*   **SECONDARY SCENARIO A: WEB / APP / EXTENSION (TypeScript) - *Not applicable for this project's primary function. Reference only for potential future web-based extensions.***
    *   **Stack:** TypeScript 6.x (Strict), Vite 7 (Rolldown), Tauri v2.x (Native), WXT (Extensions).
    *   **State:** Signals (Standardized).
    *   **Lint/Test:** Biome (Speed) + Vitest (Unit) + Playwright (E2E).
    *   **Architecture:** Feature-Sliced Design (FSD).

*   **SECONDARY SCENARIO B: SYSTEMS / PERFORMANCE (Rust/Go) - *Not applicable for this project's primary function. Reference only for potential future performance-critical components.***
    *   **Stack:** Rust (Cargo) or Go (Modules).
    *   **Lint:** Clippy / GolangCI-Lint.
    *   **Architecture:** Hexagonal Architecture (Ports & Adapters).

---

## 4. ARCHITECTURAL PRINCIPLES (The "Zen of Apex")
*   **SOLID Principles:** Ensure Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion are applied rigorously.
*   **DRY (Don't Repeat Yourself):** Minimize redundant code and configurations.
*   **YAGNI (You Aren't Gonna Need It):** Build only what is necessary for the current requirements.
*   **Clean Code:** Prioritize readability, maintainability, and testability.
*   **Observability:** Implement robust logging, metrics, and tracing for monitoring.
*   **Security by Design:** Threat modeling, secure coding practices, and regular security audits.
*   **Scalability & Resilience:** Design for high availability and graceful degradation.

---

## 5. DEVELOPMENT WORKFLOW & VERIFICATION COMMANDS
*   **Dependency Management:** `uv` is the primary tool.
    *   Install: `uv pip install -r requirements.txt`
    *   Sync: `uv pip sync`
    *   Update: `uv pip install --update-all`
*   **Linting & Formatting:** `Ruff` is mandatory.
    *   Check (no fix): `uv run ruff check .`
    *   Format (check only): `uv run ruff format . --check`
    *   Format (fix): `uv run ruff format .`
    *   Check & Fix All: `uv run ruff check --fix . && uv run ruff format .`
*   **Testing:** `Pytest` is the standard.
    *   Run all tests: `uv run pytest`
    *   Run specific test: `uv run pytest tests/unit/test_example.py`
    *   Run tests with coverage: `uv run pytest --cov=src/torrentscout --cov-report=term-missing`
*   **CI/CD Verification:** All pushes to `main` **MUST** trigger `.github/workflows/ci.yml`.
    *   **Stages:** `lint`, `test`, `build` (if applicable), `deploy` (if applicable).
    *   **Quality Gates:** 100% lint pass, 90%+ test coverage.
*   **Local Development Server:** `uv run python src/torrentscout/main.py --help` (or relevant command for testing plugins locally)
*   **Containerization (Optional but Recommended):** Dockerize the environment for consistency.
    *   Build: `docker build -t torrentscout:latest .`
    *   Run: `docker run torrentscout:latest`

---

## 6. PROJECT CONVENTIONS
*   **Naming:** Use `snake_case` for Python identifiers, `PascalCase` for classes.
*   **Docstrings:** Google style for modules, classes, and functions.
*   **Type Hinting:** Mandatory for all function parameters and return types.
*   **Error Handling:** Use custom exceptions where appropriate, ensure robust `try...except` blocks.
*   **Logging:** Use Python's `logging` module.

</details>

## udos

*   **Universal Design:** Ensure accessibility and ease of use for a broad range of users.
*   **Documentation:** Maintain comprehensive and up-to-date documentation for all features and APIs.
*   **Open Source First:** Promote community engagement and collaborative development.
