from .food import *
from .enemies import *

LEVEL1 = [
    # first wave
    {
        "tutorial": True,
        "food":[Pizza(), Apple()],
        "enemies":[
            AntEater(delay=x*AntEater.DELAY) 
            for x in range(random.randint(1, 3)) # one wave
            for _ in range(3) # waves
        ]
    },
    # second wave
    {
        "tutorial": True,
        "food":[Pizza(), Apple(), Apple(), Pizza()],
        "enemies":[
            AntEater(delay=x*AntEater.DELAY) 
            for _ in range(random.randint(2, 4)) # one wave
            for x in range(5) # waves
        ]
    }
]


LEVELS = [
    LEVEL1
]