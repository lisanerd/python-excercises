
import random

DICE1 = """
     _______
    |       |
    |   1   |
    |_______|
"""

DICE2 = """
     _______
    |       |
    |   2   |
    |_______|
"""

DICE3 = """
     _______
    |       |
    |   3   |
    |_______|
"""

DICE4 = """
     _______
    |       |
    |   4   |
    |_______|
"""

DICE5 = """
     _______
    |       |
    |   1   |
    |_______|
"""

DICE6 = """
     _______
    |       |
    |   6   |
    |_______|
"""


DICE_SIDES = [DICE1, DICE2, DICE3, DICE4, DICE5, DICE6]



print(random.choice(DICE_SIDES))



