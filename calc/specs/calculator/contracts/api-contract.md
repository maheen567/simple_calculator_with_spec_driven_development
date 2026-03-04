# API Contract: Python CLI Calculator

## 1. `Parser` Interface
Handles the conversion of raw string input into a list of RPN tokens.

- **`tokenize(raw_input: str) -> list[Token]`**
    - **Description**: Splits the input into individual tokens.
    - **Errors**: `ValueError("Invalid expression.")` if unrecognized characters are found.
- **`shunting_yard(tokens: list[Token]) -> list[Token]`**
    - **Description**: Reorders tokens into Reverse Polish Notation (RPN).
    - **Errors**: `ValueError("Invalid expression.")` if the expression is syntactically malformed.

## 2. `Evaluator` Interface
Performs arithmetic calculations on RPN tokens.

- **`evaluate(rpn_tokens: list[Token], state: SessionState) -> float`**
    - **Description**: Consumes RPN tokens and produces a result.
    - **Errors**:
        - `ZeroDivisionError("Division by zero is undefined.")`
        - `ValueError("Invalid expression.")` (for stack issues)
        - `OverflowError("Result too large.")`
        - `TypeError("Input must be numeric.")`

## 3. `CLI` Interface
Manages the REPL cycle.

- **`run_repl() -> None`**
    - **Description**: Starts the interactive prompt.
- **`format_result(value: float) -> str`**
    - **Description**: Rounds to 10 decimal places and returns a display string.
- **`handle_command(cmd: str, state: SessionState) -> None`**
    - **Description**: Processes `exit`, `quit`, `help`.

## 4. Error Mapping

| Exception | Display Message |
|-----------|-----------------|
| `ZeroDivisionError` | `Error: Division by zero is undefined.` |
| `OverflowError` | `Error: OverflowError` |
| `ValueError` | `Error: Invalid expression.` |
| `TypeError` | `Error: Input must be numeric.` |
