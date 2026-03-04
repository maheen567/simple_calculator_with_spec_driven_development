# Data Model: Python CLI Calculator

## Entities

### `SessionState` (Dataclass)
Represents the current REPL session state.
- `ans`: `float | None` - Stores the last successfully calculated result.
- `is_running`: `bool` - Tracks if the REPL should continue.

### `Token` (Dataclass)
Represents a single lexical token.
- `value`: `str` - The literal text (e.g., "3", "+", "ans").
- `type`: `TokenType` (Enum) - The type of token.

### `TokenType` (Enum)
- `NUMBER`
- `OPERATOR`
- `CONSTANT`
- `VARIABLE`
- `COMMAND`

## Precedence Rules (for Shunting-yard)

| Operator | Precedence | Associativity |
|----------|------------|---------------|
| `**`     | 4          | Right         |
| `*`      | 3          | Left          |
| `/`      | 3          | Left          |
| `//`     | 3          | Left          |
| `%`      | 3          | Left          |
| `+`      | 2          | Left          |
| `-`      | 2          | Left          |

## Validation Rules
1.  **Numeric Input**: Must be valid integer or float.
2.  **Operator Input**: Must be in the recognized set `{+, -, *, /, **, //, %}`.
3.  **Variable Input**: Only `ans`, `pi`, and `e` are permitted.
4.  **No Parentheses**: Inputs containing `(` or `)` should trigger an `Error: Invalid expression.` (or specific error for parentheses if desired).
