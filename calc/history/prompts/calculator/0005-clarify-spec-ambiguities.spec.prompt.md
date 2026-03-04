# PHR - Clarify calculator specification ambiguities

- **ID:** 0005
- **Title:** Clarify calculator specification ambiguities
- **Stage:** spec
- **Date:** 2026-03-04
- **Feature:** calculator

## Prompt
Identify underspecified areas in the current feature spec by asking up to 5 highly targeted clarification questions and encoding answers back into the spec.

## Response
I identified and resolved 5 critical ambiguities:
1. **Grouping:** Parentheses `()` will NOT be supported.
2. **Statefulness:** The `ans` variable will reference the last result.
3. **Special Values:** `inf` and `nan` will use default Python string representation.
4. **Implementation:** A "Safe Parser" will be used instead of `eval()`.
5. **Constants:** Added support for `pi` and `e`.

## Outcomes
- Updated `specs/calculator/spec.md` with explicit functional and implementation constraints.
- Reduced downstream risk by ruling out `eval()` early.
