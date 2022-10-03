
import random


class SmartDice:
    DICE_N = """         _______
        |       |
        |  {:2d}   |
        |_______|"""

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
        print(self.DICE_N.format(self.all_throws[-1]))
    
    def draw_all_throws(self):
        for a in self.all_throws:
            self.draw(s)


#########################################

# tot = throw_dice()
# tot = throw_dice(number_of_dice=2, dice_sides_number=24)

dice_1 = SmartDice()
dice_2 = SmartDice()

dice_1.throw()
dice_1.throw()
dice_1.throw()
dice_1.throw()
dice_2.throw()

tot = dice_1.sum_of_all_throw_ever

print(dice_1.all_throws, dice_2.all_throws)
# throw_dice()
# throw_dice(3)


dice_1.draw()
dice_2.draw()
print(f"Your total dice sum is {tot}")
