# J0hanz Gitpod Template

[![GitHub last commit](https://img.shields.io/github/last-commit/j0hanz/j0hanz-gitpod-template)](https://github.com/j0hanz/j0hanz-gitpod-template/commits/main)[![GitHub repo size](https://img.shields.io/github/repo-size/j0hanz/j0hanz-gitpod-template)](https://github.com/j0hanz/j0hanz-gitpod-template)

---

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/j0hanz/j0hanz-gitpod-template)

A pre-configured development environment for **Python**, **Django**, **Node.js**, **MongoDB**, **PostgreSQL**, and **Heroku** deployments. Equipped with essential tools, linters, formatters, and VS Code extensions to supercharge your workflow. ✨

---

## ✨ Features

- **Python**: `3.12.7` & `3.13.0` installed via `pyenv`
- **Node.js**: `20.18.0` installed via `nvm`
- **MongoDB Shell**: `mongosh` for database interaction
- **PostgreSQL**: `16` pre-installed and configurable
- **Heroku CLI**: For seamless deployment to Heroku
- **VS Code Extensions**: Pre-installed extensions for Python, Django, and more
- **Linters & Formatters**: `djlint` for Django, `ruff` for Python
- **Custom Scripts**: For initialization and repo info display

---

## 🚀 Getting Started

### Prerequisites

- Create a [Gitpod Account](https://www.gitpod.io/)
- Access the [repository](https://github.com/j0hanz/j0hanz-gitpod-template)

### Launch the Workspace

1. **Start**: Click the button below to open in Gitpod:

   [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/j0hanz/j0hanz-gitpod-template)

2. **Build**: Workspace builds automatically using `.gitpod.yml` and `.gitpod.Dockerfile`
3. **Initialize**: Setup runs scripts to install dependencies and extensions

---

## 🛠 Environment Details

### Python Setup

- **Versions**: 3.12.7 (default) and 3.13.0 (via `pyenv`)
- **Global Tools**:
  - `bandit`, `coverage`, `djlint`, `ruff`, `pytest`, `mypy`, `isort`, `pylint`, and more
- **Aliases**:
  - `python` → Python 3.12.7
  - `pip` → Corresponding pip version

---

### Node.js Setup

- **Version**: 20.18.0 (via `nvm`)
- **Global Tools**:
  - `npm`, `pnpm`, `yarn`, `typescript`, `eslint`, `prettier`, and `node-gyp`

---

### PostgreSQL Setup

- **Version**: PostgreSQL 16
- **Scripts**:
  - Start: `~/.pg_ctl/bin/pg_start`
  - Stop: `~/.pg_ctl/bin/pg_stop`

---

### MongoDB Shell

- Installed: `mongosh` for database interaction

---

### VS Code Extensions

- Python: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- Linters: [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff), [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- Markdown: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- Utilities: [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme), [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)

---

## ⚡ Linters & Formatters

### **djlint**: Django Template Linter

- **Config**: In `pyproject.toml`
- **Usage**:

  ```bash
  djlint templates/
  djlint --reformat templates/
  ```

### **ruff**: Fast Python Linter

- **Config**: In `pyproject.toml`
- **Usage**:

  ```bash
  ruff check .
  ruff check . --fix
  ```

---

## 📜 Custom Scripts

- **Initialization Script**: Automates dependency installation and environment setup
- **Repo Info Display**: Provides repository and branch details, last commit info, and user metadata

---

## 📄 Git Ignore

Key exclusions:

- Python: `__pycache__/`, `.pytest_cache`, `db.sqlite3`
- Node.js: `node_modules/`
- Environment: `.env`, `env.py`

---

This template is your all-in-one solution for efficient, robust development. Start building without worrying about setup.

🚀 **Happy Coding!** 🚀
