import random

y = random.randint(0,10)

count = 0

while count <= 3:
    count += 1
    player_guess = int(input("Your guess: "))
    if player_guess == y:
        print(f"You won! The secret number was {y}.")
        break
    elif player_guess < y and count != 3:
        print(f"Wrong guess. The secret number is greater than {player_guess}.")
        continue
    elif player_guess > y and count != 3:
        print(f"Wrong guess. The secret number is lesser than {player_guess}.")
        continue
    elif count == 3:
        print(f"You have no more guesses left! The secret number was {y}.")
        break


