# debug-actions

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/debug-actions/ci.yaml)](https://github.com/atloo1/debug-actions/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fdebug-actions%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.requires-python&label=python)](https://github.com/atloo1/debug-actions/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fdebug-actions%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=python)](https://github.com/atloo1/debug-actions/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/debug-actions)](https://github.com/atloo1/debug-actions/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/debug-actions)

[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](https://docs.docker.com/get-started/get-docker/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

## development

### 1st time setup

#### test locally (preemptively pass the corresponding GitHub action)

```
uv run pytest
```

```
uv run python -m src.debug_actions.main
uv run pytest tests/main_test.py
```

INTENTIONAL NON BLANK LAST LINE TO TRIGGER MDFORMAT
