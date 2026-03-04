# Python CLI Calculator

A secure, command-line calculator with a custom safe parser.

## Features

- **Basic Arithmetic:** Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced Arithmetic:** Exponentiation (**), Floor Division (//), Modulo (%)
- **Mathematical Constants:** `pi`, `e`
- **Statefulness:** Reference the last successful result using `ans`
- **Security:** Safe parser that does not use `eval()`
- **Precision:** Results rounded to 10 decimal places

## Installation

This project uses `uv` for dependency management.

```bash
# Clone the repository
git clone <repo-url>
cd calc

# Run the calculator
uv run src/calculator/__main__.py
```

## Usage

Start the calculator and enter expressions at the prompt:

```text
Python CLI Calculator. Type 'help' for commands, 'exit' to quit.
calc > 10 + 5
15.0
calc > ans * 2
30.0
calc > pi * (2 ** 3)
Error: Invalid expression. Parentheses are not supported.
calc > pi * 2 ** 3
25.1327412287
calc > help
...
calc > exit
```

## Testing

Run tests using `pytest`:

```bash
uv run pytest
```

Check coverage:

```bash
uv run pytest --cov=src/calculator
```
