# Pull Request Template

**Please ensure your pull request adheres to the following guidelines:**

## 1. Pull Request Type

*   [ ] Bug fix
*   [ ] New feature
*   [ ] Documentation update
*   [ ] Refactor
*   [ ] Other (please specify):

## 2. Description

Provide a concise and clear description of the changes introduced in this pull request. Explain the problem being solved or the new functionality being added.

## 3. Motivation

Explain why these changes are necessary. What problem does this PR solve? What is the impact of this change?

## 4. Solution

Describe the technical approach taken to implement the changes. How does this PR address the motivation?

## 5. Related Issues

Link to any relevant GitHub issues (e.g., `Fixes #123`, `Closes #456`).

## 6. Testing

*   [ ] Unit tests have been added or updated.
*   [ ] Integration tests have been added or updated.
*   [ ] Manual testing has been performed.

Describe the testing strategy and results. If tests were added, please specify their scope.

## 7. Architectural Alignment (Apex Standard)

This pull request aligns with the **Apex Technical Authority's** principles and the project's adopted stack:

*   **Stack:** Python 3.10+, uv, Ruff, Pytest.
*   **Architecture:** Modular Monolith.
*   **Linting/Formatting:** Enforced by Ruff.
*   **Testing:** Covered by Pytest.

All changes are validated against these standards.

## 8. Code Quality & Linting

*   [ ] The code adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/) and project-specific linting rules.
*   [ ] `ruff check .` passes without errors.
*   [ ] `ruff format .` has been run.

## 9. CI/CD Status

All CI checks (linting, testing, building) must pass before merging.

## 10. Developer Agreement

By submitting this pull request, I agree to the terms outlined in the `LICENSE` file and adhere to the contributing guidelines in `.github/CONTRIBUTING.md`.

---

**Thank you for your contribution to `qBittorrent-Torrent-Search-Plugin-Python-Lib`!**
