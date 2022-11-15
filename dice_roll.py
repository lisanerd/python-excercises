
from operator import truediv
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


class Game:
    def __init__(self, goal) -> None:
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.dice = SmartDice(sides=6)
        self.goal=goal
    
    def finished(self):
        if self.score_player_1 > self.goal or self.score_player_2 > self.goal:
            return True
        return False
    
    def play_turn(self):
        v1 = self.dice.throw()
        self.score_player_1 += v1
        v2 = self.dice.throw()
        self.score_player_2 += v2

    def announce(self):
        if self.score_player_1 > self.score_player_2:
            print("The winner is player 1!")
        elif self.score_player_2 > self.score_player_1:
            print("The winner is player 2!")
        else:
            print("It's a draw!")

my_game = Game(goal=20)
while not my_game.finished():
    my_game.play_turn()
my_game.announce()

sec_game = Game(40)
while not sec_game.finished():
    sec_game.play_turn()
sec_game.announce()


class GameSpecial(Game):
    def play_turn(self):
        super().play_turn()
        self.score_player_1 += 1


brand_new_game = GameSpecial(40)
while not brand_new_game.finished():
    brand_new_game.play_turn()
brand_new_game.announce()
