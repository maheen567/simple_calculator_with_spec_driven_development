# Implementation Plan: Python CLI Calculator

**Branch**: `master` | **Date**: 2026-03-04 | **Spec**: [specs/calculator/spec.md](specs/calculator/spec.md)
**Input**: Feature specification from `specs/calculator/spec.md`

## Summary
Implement a secure, CLI-based REPL calculator in Python 3.12+. The core focus is on a "safe" custom parser that implements standard mathematical precedence for basic and advanced arithmetic without using `eval()`. It will support constants (`pi`, `e`), statefulness via `ans`, and robust error handling.

## Technical Context

**Language/Version**: Python 3.12+ (Type hints mandatory)
**Primary Dependencies**: Standard Library (`math`, `re`, `shlex`), `uv` (manager), `pytest` (testing)
**Storage**: N/A (In-memory session state)
**Testing**: `pytest` (TDD: Red-Green-Refactor)
**Target Platform**: CLI / Terminal
**Project Type**: Single project (CLI)
**Performance Goals**: Instant evaluation (<10ms) for expressions.
**Constraints**: **Strictly No `eval()`**. No support for parentheses. Display rounded to 10 decimal places.
**Scale/Scope**: ~5-10 core classes/modules.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **TDD approach**: Mandatory. Tests must be written and fail first.
- [x] **Python 3.12+**: Confirmed. Using `uv` for environment management.
- [x] **Clean Code**: Adherence to PEP 8 and clean abstractions.
- [x] **ADRs**: Required for Parser implementation and REPL architecture.
- [x] **SOLID/DRY/KISS**: Simple parser design (no parentheses) aligns with KISS.

## Project Structure

### Documentation (this feature)

```text
specs/calculator/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (Interface definitions)
└── tasks.md             # Phase 2 output (to be generated)
```

### Source Code (repository root)

```text
src/calculator/
├── __init__.py
├── __main__.py          # Entry point
├── cli.py               # REPL loop
├── parser.py            # Expression parsing logic
├── evaluator.py         # Arithmetic logic
├── constants.py         # pi, e, etc.
└── models.py            # Session state / Dataclasses

tests/
├── unit/
│   ├── test_parser.py
│   ├── test_evaluator.py
│   └── test_cli.py
├── integration/
│   └── test_repl_flow.py
└── conftest.py
```

**Structure Decision**: Single project structure is optimal for this CLI tool. Logic is separated into parsing, evaluation, and CLI interaction to follow SOLID principles.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
