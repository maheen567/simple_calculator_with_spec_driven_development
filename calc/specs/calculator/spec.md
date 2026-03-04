# Specification: Python CLI Calculator

## 1. Overview
A robust command-line interface (CLI) calculator implemented in Python, supporting basic and advanced arithmetic operations with graceful error handling.

## 2. Clarifications

### Session 2026-03-04
- Q: Should the calculator support grouping with parentheses? → A: No support for grouping with parentheses.
- Q: Should the calculator support a variable to reference the last result? → A: Yes, using 'ans'.
- Q: Use custom display strings for 'inf'/'nan'? → A: No, use default Python strings.
- Q: Which parsing method should be used? → A: A Safe Parser (no eval).
- Q: Support mathematical constants like 'pi' and 'e'? → A: Yes.

## 3. Requirements

### 3.1 Operations Supported
- **Basic Arithmetic:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
- **Advanced Arithmetic:** Exponentiation (`**`), Floor Division (`//`), Modulo (`%`).
- **Constants:** `pi` (3.14159...) and `e` (2.71828...).
- **Precedence:** Standard mathematical operator precedence (e.g., exponentiation > multiplication/division > addition/subtraction) applies. **Note: Grouping with parentheses `()` is NOT supported.**

### 3.2 Interface (CLI REPL)
- The application should start a Read-Eval-Print Loop (REPL).
- User enters an expression (e.g., `10 + 5`).
- **Statefulness:** The result of the last successful calculation is stored and can be referenced in the next expression using the keyword `ans`.
- Special commands: `exit`, `quit`, `help`.

### 3.3 Evaluation & Parsing
- **Implementation:** The calculator must use a custom, safe parser (e.g., based on `shlex` or `re`) rather than Python's `eval()`.
- **Security:** The parser must only allow registered operators, numeric values, and recognized constants/variables (`ans`, `pi`, `e`).

### 3.4 Floating-Point & Precision
- **Internal Representation:** Use Python's native `float` (IEEE 754).
- **Display Precision:** Results rounded to 10 decimal places for display.
- **Special Values:** `inf` and `nan` displayed using Python's default string representation.

### 3.5 Error Handling & Edge Cases
- **Division by Zero:** Display `Error: Division by zero is undefined.`
- **Invalid Input:** Display `Error: Invalid expression.` for malformed syntax.
- **Non-Numeric Input:** Display `Error: Input must be numeric.` (ignoring constants/commands).
- **Overflow:** Gracefully handle `OverflowError`.

## 4. Acceptance Criteria
- [ ] Successfully performs all basic and advanced operations.
- [ ] REPL starts, accepts input, and exits correctly.
- [ ] `ans` correctly stores and retrieves the previous result.
- [ ] `pi` and `e` constants are recognized and accurate.
- [ ] Division by zero does not crash the program.
- [ ] Parser is confirmed as "safe" (does not use `eval()`).
- [ ] Parentheses return an error or are ignored as invalid characters.
