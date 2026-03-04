import sys
from pathlib import Path

# Add src to sys.path to resolve imports when run directly as a script
src_path = Path(__file__).resolve().parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from calculator.cli import run_repl

if __name__ == "__main__":
    run_repl()
