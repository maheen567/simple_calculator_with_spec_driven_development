import sys
import math
from calculator.models import SessionState, TokenType
from calculator.parser import Parser
from calculator.evaluator import Evaluator
from calculator.constants import DISPLAY_PRECISION

def format_result(value: float) -> str:
    """Format the result to a maximum of DISPLAY_PRECISION decimal places."""
    res = round(value, DISPLAY_PRECISION)
    # If it's a whole number, return as .0
    if res == int(res):
        return f"{float(res)}"
    return str(res)

def handle_command(cmd: str, state: SessionState) -> bool:
    """Handle special commands like exit, quit, help. Returns True if handled."""
    c = cmd.strip().lower()
    if c in ['exit', 'quit']:
        state.is_running = False
        return True
    elif c == 'help':
        print("\nPython CLI Calculator Help:")
        print("Basic Ops: +, -, *, /")
        print("Advanced Ops: **, //, %")
        print("Constants: pi, e")
        print("Variables: ans (previous result)")
        print("Commands: help, exit, quit\n")
        return True
    return False

def run_repl():
    state = SessionState()
    parser = Parser()
    evaluator = Evaluator()
    
    print("Python CLI Calculator. Type 'help' for commands, 'exit' to quit.")
    
    while state.is_running:
        try:
            user_input = input("calc > ").strip()
            if not user_input:
                continue
            
            if handle_command(user_input, state):
                continue
            
            # Tokenize and evaluate
            tokens = parser.tokenize(user_input)
            rpn = parser.shunting_yard(tokens)
            result = evaluator.evaluate(rpn, state)
            
            print(format_result(result))
            
        except EOFError:
            print("\nExiting...")
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except OverflowError:
            print("Error: OverflowError")
        except ValueError as e:
            msg = str(e)
            if not msg.startswith("Error:"):
                msg = f"Error: {msg}"
            print(msg)
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_repl()
