import math
from enum import Enum, auto

class Associativity(Enum):
    LEFT = auto()
    RIGHT = auto()

# Precedence and Associativity for operators
PRECEDENCE = {
    "**": 4,
    "*": 3,
    "/": 3,
    "//": 3,
    "%": 3,
    "+": 2,
    "-": 2,
}

ASSOCIATIVITY = {
    "**": Associativity.RIGHT,
    "*": Associativity.LEFT,
    "/": Associativity.LEFT,
    "//": Associativity.LEFT,
    "%": Associativity.LEFT,
    "+": Associativity.LEFT,
    "-": Associativity.LEFT,
}

# Mathematical constants
CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

# Rounded precision for display
DISPLAY_PRECISION = 10
