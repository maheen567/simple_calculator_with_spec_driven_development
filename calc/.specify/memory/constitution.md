<!--
Sync Impact Report:
- Version change: N/A -> 1.0.0
- List of modified principles: All principles updated/added based on user input.
- Added sections: Technical Stack, Quality Requirements
- Removed sections: Original template placeholder principles (adjusted to 5 principles).
- Templates requiring updates:
    - .specify/templates/plan-template.md ⚠ pending
    - .specify/templates/spec-template.md ⚠ pending
    - .specify/templates/tasks-template.md ⚠ pending
    - .specify/templates/commands/*.md ⚠ pending
- Follow-up TODOs: None
-->
# Gemini CLI Project Constitution

## Core Principles

### I. Write tests first (TDD approach)
TDD is mandatory: Tests MUST be written before implementation, reviewed, and MUST fail before any new code is introduced. The Red-Green-Refactor cycle MUST be strictly enforced.

### II. Use Python 3.12+ with type hints everywhere
All Python code MUST use Python 3.12 or newer. Type hints are mandatory for all function signatures and variable declarations to ensure code clarity and maintainability.

### III. Keep code clean and easy to read
Code MUST be self-documenting where possible, adhering to established style guides (e.g., PEP 8) and minimizing complexity. Readability is paramount for collaboration and long-term maintainability.

### IV. Document important decisions with ADRs
Architecturally significant decisions MUST be documented using Architectural Decision Records (ADRs) to capture context, options considered, trade-offs, and rationale.

### V. Follow essential OOP principles: SOLID, DRY, KISS
Object-Oriented Programming (OOP) principles including SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid) MUST be applied to ensure robust, maintainable, and scalable code.

## Technical Stack

- Python 3.12+ with UV package manager
- pytest for testing
- Keep all project files in git

## Quality Requirements

- All tests MUST pass
- At least 80% code coverage MUST be maintained
- Use dataclasses for data structures

## Governance

Amendments to this constitution require a documented proposal, review by core contributors, and explicit approval. All code changes MUST adhere to these principles. Compliance will be reviewed regularly.

**Version**: 1.0.0 | **Ratified**: 2026-03-03 | **Last Amended**: 2026-03-03
