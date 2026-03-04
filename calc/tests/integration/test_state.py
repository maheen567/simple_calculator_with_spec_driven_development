import pytest
from calculator.parser import Parser
from calculator.evaluator import Evaluator
from calculator.models import SessionState

def test_ans_persistence():
    parser = Parser()
    evaluator = Evaluator()
    state = SessionState()
    
    # First calculation: 10 + 5 = 15
    tokens = parser.tokenize("10 + 5")
    rpn = parser.shunting_yard(tokens)
    result = evaluator.evaluate(rpn, state)
    assert result == 15.0
    state.ans = result # CLI will do this
    
    # Second calculation: ans * 2 = 30
    tokens = parser.tokenize("ans * 2")
    rpn = parser.shunting_yard(tokens)
    result = evaluator.evaluate(rpn, state)
    assert result == 30.0
    state.ans = result
    
    # Third calculation: ans - 5 = 25
    tokens = parser.tokenize("ans - 5")
    rpn = parser.shunting_yard(tokens)
    result = evaluator.evaluate(rpn, state)
    assert result == 25.0
