
import random



class SmartDice:
    def __init__(self, sides=6) -> None:
        self.sides = sides
        self.sum_of_all_throw_ever = 0
        self.all_throws = []

    def throw(self):
        number = random.randint(1, self.sides)
        self.all_throws.append(number)
        self.sum_of_all_throw_ever += number
        return number

    def draw(self):
        pass


DICE_N = """     _______
    |       |
    |   {}   |
    |_______|"""

def throw_dice(number_of_dice:int = 1, dice_sides_number = 6):
    print('-'*8)
    total = 0
    for d in range(number_of_dice):
        number = random.randint(1, dice_sides_number)
        face = DICE_N.format(number)
        print(face)
        total += number
    return total

#########################################

# tot = throw_dice()
# tot = throw_dice(number_of_dice=2, dice_sides_number=24)

dice_1 = SmartDice(sides=8)
dice_2 = SmartDice(sides=32)

dice_1.throw()
dice_1.throw()
dice_1.throw()
dice_1.throw()
dice_2.throw()

tot = dice_1.sum_of_all_throw_ever + dice_2.sum_of_all_throw_ever

print(dice_1.all_throws, dice_2.all_throws)
# throw_dice()
# throw_dice(3)


print(f"Your total dice sum is {tot}")
