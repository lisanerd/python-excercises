
import random



DICE_SIDES_NUMBER = 6

DICE_N = """     _______
    |       |
    |   {}   |
    |_______|"""

def throw_dice(number_of_dice:int = 1):
    print('-'*8)
    total = 0
    for d in range(number_of_dice):
        number = random.randint(1, DICE_SIDES_NUMBER)
        face = DICE_N.format(number)
        print(face)
        total += number
    return total

#########################################

tot = throw_dice(number_of_dice=2)
# throw_dice()
# throw_dice(3)


print(f"Your total dice sum is {tot}")
