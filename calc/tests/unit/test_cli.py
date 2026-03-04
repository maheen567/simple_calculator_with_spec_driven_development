import pytest
from unittest.mock import patch, MagicMock
from calculator.cli import handle_command, format_result
from calculator.models import SessionState

def test_format_result():
    assert format_result(1.2345678901234) == "1.2345678901"
    assert format_result(1.0) == "1.0"
    assert format_result(math.pi) == "3.1415926536"

def test_handle_command_exit():
    state = SessionState()
    handle_command("exit", state)
    assert state.is_running is False

def test_handle_command_quit():
    state = SessionState()
    handle_command("quit", state)
    assert state.is_running is False

import math
