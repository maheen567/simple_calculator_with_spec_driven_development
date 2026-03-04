import pytest
from unittest.mock import patch, MagicMock
from calculator.cli import run_repl

def test_repl_basic_flow():
    # Mock input to provide a sequence of commands then exit
    inputs = ["10 + 5", "ans * 2", "exit"]
    with patch('builtins.input', side_effect=inputs) as mock_input, \
         patch('builtins.print') as mock_print:
        run_repl()
        
        # Check if results were printed
        # 10 + 5 = 15.0
        # 15.0 * 2 = 30.0
        
        # We look for calls to print that contain the formatted results
        printed_messages = [str(call.args[0]) for call in mock_print.call_args_list]
        assert any("15.0" in msg for msg in printed_messages)
        assert any("30.0" in msg for msg in printed_messages)

def test_repl_error_handling():
    inputs = ["1 / 0", "invalid expression", "exit"]
    with patch('builtins.input', side_effect=inputs) as mock_input, \
         patch('builtins.print') as mock_print:
        run_repl()
        
        printed_messages = [str(call.args[0]) for call in mock_print.call_args_list]
        assert any("Error: Division by zero is undefined." in msg for msg in printed_messages)
        assert any("Error: Invalid expression." in msg for msg in printed_messages)
