import re
from typing import List
from calculator.models import Token, TokenType
from calculator.constants import PRECEDENCE, ASSOCIATIVITY, Associativity

class Parser:
    def tokenize(self, raw_input: str) -> List[Token]:
        """Convert raw input string into a list of Tokens."""
        # Regex for tokens: 
        # Numbers (including decimals), operators, constants, variables
        # Note: US1 only needs basic numbers and + - * /
        # We'll implement a more complete regex now to save time
        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('OPERATOR', r'\*\*|//|[%*+/-]'), # Operators (ordered by length)
            ('PAREN',    r'[()]'),          # Parentheses (rejected)
            ('IDENT',    r'[a-zA-Z_]\w*'), # Constants or variables
            ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
            ('MISMATCH', r'.'),             # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        
        tokens = []
        for mo in re.finditer(tok_regex, raw_input):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                tokens.append(Token(value, TokenType.NUMBER))
            elif kind == 'OPERATOR':
                tokens.append(Token(value, TokenType.OPERATOR))
            elif kind == 'PAREN':
                raise ValueError("Invalid expression. Parentheses are not supported.")
            elif kind == 'IDENT':
                # Constants or variables will be handled in later US
                # For now, we'll treat them as VARIABLE or CONSTANT
                if value in ['pi', 'e']:
                    tokens.append(Token(value, TokenType.CONSTANT))
                elif value == 'ans':
                    tokens.append(Token(value, TokenType.VARIABLE))
                else:
                    # US5 might handle commands like exit, but for now they are unknown
                    tokens.append(Token(value, TokenType.COMMAND))
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise ValueError("Invalid expression.")
        return tokens

    def shunting_yard(self, tokens: List[Token]) -> List[Token]:
        """Convert infix tokens to Reverse Polish Notation (RPN)."""
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.type in (TokenType.NUMBER, TokenType.CONSTANT, TokenType.VARIABLE):
                output_queue.append(token)
            elif token.type == TokenType.OPERATOR:
                while (operator_stack and 
                       operator_stack[-1].type == TokenType.OPERATOR):
                    op1 = token.value
                    op2 = operator_stack[-1].value
                    
                    p1 = PRECEDENCE.get(op1, 0)
                    p2 = PRECEDENCE.get(op2, 0)
                    
                    if (ASSOCIATIVITY.get(op1) == Associativity.LEFT and p1 <= p2) or \
                       (ASSOCIATIVITY.get(op1) == Associativity.RIGHT and p1 < p2):
                        output_queue.append(operator_stack.pop())
                    else:
                        break
                operator_stack.append(token)
            elif token.type == TokenType.COMMAND:
                # Commands are handled by CLI, but if they appear in an expression, it's an error
                output_queue.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue
