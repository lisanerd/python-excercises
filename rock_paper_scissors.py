import random

game_list = ['rock', 'paper', 'scissors']

computer_choice = random.choice(game_list)

player_choice = input("Rock, Paper, or Scissors?: ")

if computer_choice == player_choice:
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("It's a tie!")
if computer_choice == "rock" and player_choice == "scissors":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("The computer wins!")
if computer_choice == "rock" and player_choice == "paper":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("You win!")
if computer_choice == "scissors" and player_choice == "rock":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("You win!")
if computer_choice == "scissors" and player_choice == "paper":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("The computer wins!")
if computer_choice == "paper" and player_choice == "scissors":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("You win!")
if computer_choice == "paper" and player_choice == "rock":
    print(f"Computer choice: {computer_choice}")
    print(f"Player choice: {player_choice}")
    print("The computer wins!")
