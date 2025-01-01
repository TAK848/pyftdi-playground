# pyftdi-client

## Requirements

- uv 0.5.13+
  - https://github.com/astral-sh/uv
  - python 3.13

## Setup

### env

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

### Initialize

```bash
uv python install 3.13
uv venv
source .venv/bin/activate
uv sync
```

### Always activate the virtual environment

```bash
source .venv/bin/activate
```

### Exit the virtual environment

```bash
deactivate
```

or exit the terminal and re-open it.

### Sync dependencies

```bash
uv sync
```

## Run

```bash
uv run app.py
```

## Add dependencies

For example, to add `pyftdi`:
```bash
uv add pyftdi
uv sync
```
