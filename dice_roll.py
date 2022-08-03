
import random

DICE_SIDES_NUMBER = 7

DICE_N = """
     _______
    |       |
    |   {}   |
    |_______|
"""



DICE_SIDES = [DICE_N.format(i) for i in range(1, DICE_SIDES_NUMBER)]


print(random.choice(DICE_SIDES))



