# Tasks: Python CLI Calculator

**Input**: Design documents from `specs/calculator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api-contract.md

**Tests**: TDD approach requested. Tests MUST be written and fail before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/calculator/`, `tests/unit/`, `tests/integration/`
- [X] T002 [P] Initialize Python project with `uv init` and add `pytest` dependency
- [X] T003 [P] Configure `pyproject.toml` with Python 3.12 settings and type hint requirements

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T004 Implement `TokenType` Enum and `Token` Dataclass in `src/calculator/models.py`
- [X] T005 Implement `SessionState` Dataclass in `src/calculator/models.py`
- [X] T006 [P] Define `PRECEDENCE` and `ASSOCIATIVITY` maps in `src/calculator/constants.py`
- [X] T007 Create base `Parser` class skeleton in `src/calculator/parser.py`
- [X] T008 Create base `Evaluator` class skeleton in `src/calculator/evaluator.py`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Support addition, subtraction, multiplication, and division.

**Independent Test**: Run `pytest tests/unit/test_basic_ops.py` to verify `+`, `-`, `*`, `/`.

### Tests for User Story 1 (TDD)

- [X] T009 [P] [US1] Create unit tests for basic operations in `tests/unit/test_evaluator.py`
- [X] T010 [P] [US1] Create unit tests for basic tokenization and Shunting-yard in `tests/unit/test_parser.py`

### Implementation for User Story 1

- [X] T011 [US1] Implement `tokenize` for basic numbers and `+`, `-`, `*`, `/` in `src/calculator/parser.py`
- [X] T012 [US1] Implement `shunting_yard` logic for precedence in `src/calculator/parser.py`
- [X] T013 [US1] Implement RPN evaluation for `+`, `-`, `*`, `/` in `src/calculator/evaluator.py`
- [X] T014 [US1] Add `ZeroDivisionError` handling in `src/calculator/evaluator.py`

**Checkpoint**: Basic arithmetic is fully functional and testable.

---

## Phase 4: User Story 2 - Advanced Arithmetic (Priority: P1)

**Goal**: Support exponentiation (`**`), floor division (`//`), and modulo (`%`).

**Independent Test**: Run `pytest tests/unit/test_advanced_ops.py` to verify `**`, `//`, `%`.

### Tests for User Story 2 (TDD)

- [X] T015 [X] [US2] Add unit tests for `**`, `//`, `%` in `tests/unit/test_evaluator.py`
- [X] T016 [X] [US2] Add unit tests for advanced operator tokenization in `tests/unit/test_parser.py`

### Implementation for User Story 2

- [X] T017 [US2] Update `tokenize` to support `**`, `//`, `%` in `src/calculator/parser.py`
- [X] T018 [US2] Update `shunting_yard` to handle `**` right-associativity in `src/calculator/parser.py`
- [X] T019 [US2] Implement RPN evaluation for `**`, `//`, `%` in `src/calculator/evaluator.py`

**Checkpoint**: Advanced arithmetic operations are complete.

---

## Phase 5: User Story 3 - Constants (Priority: P2)

**Goal**: Support `pi` and `e`.

**Independent Test**: Evaluate `pi * 2` and `e + 1` via unit tests.

### Tests for User Story 3 (TDD)

- [X] T020 [X] [US3] Add unit tests for constant resolution in `tests/unit/test_evaluator.py`
- [X] T021 [X] [US3] Add unit tests for `pi` and `e` tokens in `tests/unit/test_parser.py`

### Implementation for User Story 3

- [X] T022 [US3] Define `pi` and `e` values in `src/calculator/constants.py`
- [X] T023 [US3] Update `tokenize` to recognize `pi` and `e` in `src/calculator/parser.py`
- [X] T024 [US3] Update `evaluate` to substitute constants in `src/calculator/evaluator.py`

**Checkpoint**: Mathematical constants are now supported.

---

## Phase 6: User Story 4 - Statefulness (Priority: P2)

**Goal**: Support `ans` variable to reference the last result.

**Independent Test**: Evaluate `10 + 5` then `ans * 2` in an integration test.

### Tests for User Story 4 (TDD)

- [X] T025 [P] [US4] Add unit tests for `ans` tokenization in `tests/unit/test_parser.py`
- [X] T026 [P] [US4] Add integration test for `ans` persistence in `tests/integration/test_state.py`

### Implementation for User Story 4

- [X] T027 [US4] Update `tokenize` to recognize `ans` in `src/calculator/parser.py`
- [X] T028 [US4] Update `evaluate` to fetch `ans` from `SessionState` in `src/calculator/evaluator.py`
- [X] T029 [US4] Ensure `SessionState.ans` is updated after successful calculation in `src/calculator/evaluator.py`

**Checkpoint**: The calculator now maintains session state.

---

## Phase 7: User Story 5 - CLI REPL (Priority: P1)

**Goal**: Provide a Read-Eval-Print Loop with special commands.

**Independent Test**: Mock input/output to verify `exit`, `help`, and result display.

### Tests for User Story 5 (TDD)

- [X] T030 [P] [US5] Create unit tests for REPL command handling in `tests/unit/test_cli.py`
- [X] T031 [P] [US5] Create integration tests for end-to-end CLI flow in `tests/integration/test_cli_flow.py`

### Implementation for User Story 5

- [X] T032 [US5] Implement `format_result` (10 decimal places) in `src/calculator/cli.py`
- [X] T033 [US5] Implement `handle_command` for `exit`, `quit`, `help` in `src/calculator/cli.py`
- [X] T034 [US5] Implement the main REPL loop in `src/calculator/cli.py`
- [X] T035 [US5] Create entry point in `src/calculator/__main__.py`

**Checkpoint**: The CLI application is fully functional.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Error handling, cleanup, and documentation.

- [X] T036 [P] Implement global error handling for `OverflowError` and invalid syntax in `src/calculator/cli.py`
- [X] T037 [P] Update `README.md` with final usage instructions
- [X] T038 Add validation to reject parentheses `(` or `)` in `src/calculator/parser.py`
- [X] T039 Run `pytest --cov=src/calculator` and ensure 80%+ coverage
- [X] T040 Final code cleanup and PEP 8 compliance check

---

## Dependencies & Execution Order

- **Foundational (Phase 2)** must be complete before any User Story.
- **US1 & US2** can be developed in parallel after Foundation.
- **US3 & US4** can be developed in parallel after US1.
- **US5 (CLI)** depends on Evaluator and Parser logic being stable.
- **TDD Requirement**: For every US, the corresponding tests MUST be written and fail before implementation begins.

## Implementation Strategy

### MVP First
1. Setup + Foundation
2. US1 (Basic Arithmetic)
3. US5 (CLI REPL - basic version)
4. Validate MVP

### Incremental Delivery
- Add Advanced Ops (US2)
- Add Constants (US3)
- Add Statefulness (US4)
- Final Polish
