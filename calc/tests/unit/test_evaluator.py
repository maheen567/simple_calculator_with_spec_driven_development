import math
import pytest
from calculator.evaluator import Evaluator
from calculator.models import Token, TokenType, SessionState

def test_evaluate_basic_addition():
    evaluator = Evaluator()
    state = SessionState()
    # 1 + 2 in RPN: 1 2 +
    tokens = [
        Token("1", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("+", TokenType.OPERATOR)
    ]
    assert evaluator.evaluate(tokens, state) == 3.0

def test_evaluate_basic_subtraction():
    evaluator = Evaluator()
    state = SessionState()
    # 10 - 4 in RPN: 10 4 -
    tokens = [
        Token("10", TokenType.NUMBER),
        Token("4", TokenType.NUMBER),
        Token("-", TokenType.OPERATOR)
    ]
    assert evaluator.evaluate(tokens, state) == 6.0

def test_evaluate_basic_multiplication():
    evaluator = Evaluator()
    state = SessionState()
    # 3 * 7 in RPN: 3 7 *
    tokens = [
        Token("3", TokenType.NUMBER),
        Token("7", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR)
    ]
    assert evaluator.evaluate(tokens, state) == 21.0

def test_evaluate_basic_division():
    evaluator = Evaluator()
    state = SessionState()
    # 10 / 2 in RPN: 10 2 /
    tokens = [
        Token("10", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("/", TokenType.OPERATOR)
    ]
    assert evaluator.evaluate(tokens, state) == 5.0

def test_evaluate_division_by_zero():
    evaluator = Evaluator()
    state = SessionState()
    tokens = [
        Token("10", TokenType.NUMBER),
        Token("0", TokenType.NUMBER),
        Token("/", TokenType.OPERATOR)
    ]
    with pytest.raises(ZeroDivisionError, match="Division by zero is undefined."):
        evaluator.evaluate(tokens, state)

def test_evaluate_advanced_ops():
    evaluator = Evaluator()
    state = SessionState()
    
    # 2 ** 3 = 8
    tokens = [Token("2", TokenType.NUMBER), Token("3", TokenType.NUMBER), Token("**", TokenType.OPERATOR)]
    assert evaluator.evaluate(tokens, state) == 8.0
    
    # 10 // 3 = 3
    tokens = [Token("10", TokenType.NUMBER), Token("3", TokenType.NUMBER), Token("//", TokenType.OPERATOR)]
    assert evaluator.evaluate(tokens, state) == 3.0
    
    # 10 % 3 = 1
    tokens = [Token("10", TokenType.NUMBER), Token("3", TokenType.NUMBER), Token("%", TokenType.OPERATOR)]
    assert evaluator.evaluate(tokens, state) == 1.0

def test_evaluate_right_associativity():
    evaluator = Evaluator()
    state = SessionState()
    # 2 ** 3 ** 2 = 2 ** 9 = 512
    # RPN: 2 3 2 ** **
    tokens = [
        Token("2", TokenType.NUMBER),
        Token("3", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("**", TokenType.OPERATOR),
        Token("**", TokenType.OPERATOR)
    ]
    assert evaluator.evaluate(tokens, state) == 512.0

def test_evaluate_constants():
    evaluator = Evaluator()
    state = SessionState()
    
    # pi
    tokens = [Token("pi", TokenType.CONSTANT)]
    assert evaluator.evaluate(tokens, state) == math.pi
    
    # e
    tokens = [Token("e", TokenType.CONSTANT)]
    assert evaluator.evaluate(tokens, state) == math.e
    
    # pi * 2
    tokens = [Token("pi", TokenType.CONSTANT), Token("2", TokenType.NUMBER), Token("*", TokenType.OPERATOR)]
    assert evaluator.evaluate(tokens, state) == math.pi * 2
