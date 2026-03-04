---
id: 12
title: "Fix ModuleNotFoundError: No module named 'calculator'"
stage: green
date: 2026-03-04
surface: agent
model: gemini-cli
feature: calculator
branch: main
user: user
command: "uv run src/calculator/__main__.py"
labels: ["fix", "python", "package", "cli"]
links:
  spec: specs/calculator/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - src/calculator/__init__.py
 - src/calculator/__main__.py
 - pyproject.toml
tests:
 - pytest
---

## Prompt

After running this command uv run src/calculator/__main__.py , i am getting this error Traceback (most recent call last):
  File "C:\Users\maheen hussain\Desktop\calc\src\calculator\__main__.py", line 1, in <module>
    from calculator.cli import run_repl
ModuleNotFoundError: No module named 'calculator'. Fix it

## Response snapshot

I've fixed the `ModuleNotFoundError` by:
1. Adding an empty `src/calculator/__init__.py` to mark it as a package.
2. Adding a `sys.path` hack in `src/calculator/__main__.py` to allow it to find the `calculator` package when run directly as a script.
3. Adding a `[project.scripts]` entry `calc` to `pyproject.toml`, allowing you to also run the calculator via `uv run calc`.

## Outcome

- ✅ Impact: High - resolved a critical issue preventing the application from running.
- 🧪 Tests: 23/23 tests passed.
- 📁 Files: src/calculator/__init__.py, src/calculator/__main__.py, pyproject.toml
- 🔁 Next prompts: none
- 🧠 Reflection: For `src` layouts, `uv run` needs either an entry point or the `src` directory to be in the `PYTHONPATH`.

## Evaluation notes (flywheel)

- Failure modes observed: ModuleNotFoundError due to src layout.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
