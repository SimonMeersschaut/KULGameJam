from .food import *
from .enemies import *

LEVEL1 = {
    "pre-slides": [], #[1, 2, 3],
    "food": [(1, Cookie), (1, Appelsien)]
}

LEVEL2 = {
    "pre-slides": [], #[4],
    "food": [(2, Chip), (2, Snoep)]
}

LEVEL3 = {
    "pre-slides": [5],
    "food": [(3, Druif), (3, Apple)]
}

LEVEL4 = {
    "pre-slides": [6],
    "food": [(4, Croissant), (4, Bagguette)]
}

LEVEL5 = {
    "pre-slides": [7],
    "food": [(10, Pizza)]
}

LEVEL5 = {
    "pre-slides": [7],
    "food": [(1, Taart)]
}

LEVELS = [
    LEVEL1,
    LEVEL2,
    LEVEL3,
    LEVEL4,
    LEVEL5,
]