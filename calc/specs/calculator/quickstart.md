# Quickstart: Python CLI Calculator

## Prerequisites
- **Python 3.12+**
- **UV Package Manager** (Optional but recommended)
- **Pytest** (for testing)

## Installation
If you're using UV, the dependencies will be automatically managed.

```bash
# Clone and enter the project
cd calc/

# Install dependencies (if using UV)
uv sync
```

## Running the Calculator
To start the REPL:

```bash
# Using Python directly
python src/calculator/__main__.py

# Or via UV
uv run src/calculator/__main__.py
```

## Running Tests
Tests are implemented using `pytest` following a TDD workflow.

```bash
# Run all tests
pytest tests/

# Run tests with coverage
pytest --cov=src/calculator tests/
```

## Usage Examples
```text
> 10 + 5
15.0
> ans * 2
30.0
> 2 ** 3
8.0
> pi * 10
31.4159265359
> exit
```
