# Research: Python CLI Calculator

## Decision: Shunting-yard Algorithm for Precedence
**What**: The calculator will implement the Shunting-yard algorithm to convert infix expressions (e.g., `3 + 4 * 2`) to Reverse Polish Notation (RPN), which simplifies evaluation while respecting precedence.
**Rationale**: Even without parentheses, precedence rules (`**` > `*`, `/`, `//`, `%` > `+`, `-`) are more easily managed by converting to RPN than by performing multi-pass iterations over the expression. It is a robust, well-documented, and "safe" alternative to `eval()`.
**Alternatives**:
-   **Multi-pass iteration**: Evaluate higher-precedence operators first. Rejected because it's harder to maintain if more operators are added later.
-   **AST-based parsing**: Using `ast.parse` and then traversing. Rejected as it might be overkill for an expression parser without parentheses.

## Decision: Tokenization using `re`
**What**: Use Python's `re` (Regular Expressions) to tokenize the input.
**Rationale**: `re` is highly efficient for splitting expressions into numbers, operators, and identifiers like `ans`, `pi`, or `e`. Using `shlex` was considered but `re.findall` with a specific pattern (e.g., `r'\d+\.?\d*|\*\*|//|[-+*/%]|[a-zA-Z]+'`) gives more precise control over custom tokens.

## Decision: Session State via Dataclass
**What**: Use a `SessionState` dataclass to store `ans`.
**Rationale**: Aligns with the constitution's mandate to use dataclasses. Provides a clean, typed container for REPL state.

## Decision: Standard Library Constants
**What**: Use `math.pi` and `math.e`.
**Rationale**: These are industry-standard and provide the required precision.

## Best Practices for Python 3.12+ CLI
-   Use `argparse` for initial CLI entry, though the main interface is a REPL loop.
-   Use `try-except` blocks to handle specific exceptions like `ZeroDivisionError` and `OverflowError`.
-   Use `typing.Union` (`|`) and other modern type hint features.
