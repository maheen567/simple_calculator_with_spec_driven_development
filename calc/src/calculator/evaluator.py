from typing import List
from calculator.models import Token, TokenType, SessionState
from calculator.constants import CONSTANTS

class Evaluator:
    def evaluate(self, rpn_tokens: List[Token], state: SessionState) -> float:
        """Perform calculation on RPN tokens."""
        stack: List[float] = []

        for token in rpn_tokens:
            if token.type == TokenType.NUMBER:
                stack.append(float(token.value))
            elif token.type == TokenType.CONSTANT:
                stack.append(CONSTANTS[token.value])
            elif token.type == TokenType.VARIABLE:
                if token.value == 'ans':
                    if state.ans is None:
                        # If ans is not set, we can either raise an error or treat as 0
                        # The spec doesn't specify. Let's raise ValueError.
                        raise ValueError("Error: 'ans' is not yet defined.")
                    stack.append(state.ans)
            elif token.type == TokenType.OPERATOR:
                if len(stack) < 2:
                    raise ValueError("Error: Invalid expression.")
                b = stack.pop()
                a = stack.pop()
                
                result = self._apply_operator(a, b, token.value)
                stack.append(result)
            elif token.type == TokenType.COMMAND:
                # Commands shouldn't be here in a valid expression
                raise ValueError("Error: Invalid expression.")

        if len(stack) != 1:
            raise ValueError("Error: Invalid expression.")
        
        result = stack[0]
        state.ans = result
        return result

    def _apply_operator(self, a: float, b: float, op: str) -> float:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return a / b
        elif op == '//':
            if b == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return a // b
        elif op == '%':
            if b == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return a % b
        elif op == '**':
            return a ** b
        else:
            raise ValueError(f"Unknown operator: {op}")
