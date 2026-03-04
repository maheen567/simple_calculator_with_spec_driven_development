from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    CONSTANT = auto()
    VARIABLE = auto()
    COMMAND = auto()

@dataclass(frozen=True)
class Token:
    value: str
    type: TokenType

@dataclass
class SessionState:
    ans: Optional[float] = None
    is_running: bool = True
