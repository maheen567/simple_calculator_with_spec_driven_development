import pytest
from calculator.parser import Parser
from calculator.models import Token, TokenType

def test_tokenize_basic():
    parser = Parser()
    tokens = parser.tokenize("1 + 2 * 3")
    assert tokens == [
        Token("1", TokenType.NUMBER),
        Token("+", TokenType.OPERATOR),
        Token("2", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER)
    ]

def test_shunting_yard_basic():
    parser = Parser()
    # Infix: 1 + 2 * 3
    # RPN: 1 2 3 * +
    tokens = [
        Token("1", TokenType.NUMBER),
        Token("+", TokenType.OPERATOR),
        Token("2", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER)
    ]
    rpn = parser.shunting_yard(tokens)
    assert rpn == [
        Token("1", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("3", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR),
        Token("+", TokenType.OPERATOR)
    ]

def test_shunting_yard_precedence():
    parser = Parser()
    # Infix: 1 * 2 + 3
    # RPN: 1 2 * 3 +
    tokens = [
        Token("1", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR),
        Token("2", TokenType.NUMBER),
        Token("+", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER)
    ]
    rpn = parser.shunting_yard(tokens)
    assert rpn == [
        Token("1", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("*", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER),
        Token("+", TokenType.OPERATOR)
    ]

def test_tokenize_invalid_character():
    parser = Parser()
    with pytest.raises(ValueError, match="Invalid expression."):
        parser.tokenize("1 + 2 $ 3")

def test_tokenize_advanced():
    parser = Parser()
    tokens = parser.tokenize("2 ** 3 // 4 % 5")
    assert tokens == [
        Token("2", TokenType.NUMBER),
        Token("**", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER),
        Token("//", TokenType.OPERATOR),
        Token("4", TokenType.NUMBER),
        Token("%", TokenType.OPERATOR),
        Token("5", TokenType.NUMBER)
    ]

def test_shunting_yard_right_assoc():
    parser = Parser()
    # Infix: 2 ** 3 ** 2
    # RPN: 2 3 2 ** **
    tokens = [
        Token("2", TokenType.NUMBER),
        Token("**", TokenType.OPERATOR),
        Token("3", TokenType.NUMBER),
        Token("**", TokenType.OPERATOR),
        Token("2", TokenType.NUMBER)
    ]
    rpn = parser.shunting_yard(tokens)
    assert rpn == [
        Token("2", TokenType.NUMBER),
        Token("3", TokenType.NUMBER),
        Token("2", TokenType.NUMBER),
        Token("**", TokenType.OPERATOR),
        Token("**", TokenType.OPERATOR)
    ]

def test_tokenize_constants():
    parser = Parser()
    tokens = parser.tokenize("pi + e")
    assert tokens == [
        Token("pi", TokenType.CONSTANT),
        Token("+", TokenType.OPERATOR),
        Token("e", TokenType.CONSTANT)
    ]

def test_tokenize_ans():
    parser = Parser()
    tokens = parser.tokenize("ans * 2")
    assert tokens == [
        Token("ans", TokenType.VARIABLE),
        Token("*", TokenType.OPERATOR),
        Token("2", TokenType.NUMBER)
    ]

def test_tokenize_parentheses_rejected():
    parser = Parser()
    with pytest.raises(ValueError, match="Invalid expression. Parentheses are not supported."):
        parser.tokenize("(1 + 2)")
