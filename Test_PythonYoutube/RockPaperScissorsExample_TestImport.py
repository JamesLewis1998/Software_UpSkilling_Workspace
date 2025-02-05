#RockPaperScissors Programming Example Test Import

import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice rock, paper, scissors:")
    computer_choice = random.choice (options)
    choices = {"player": player_choice, "computer" : computer_choice}
    return choices

def check_win (player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a Tie"
    elif player == "rock":
        if computer == "scissors":
            return "Player wins"
        else:
            return "You lose"
    elif player == "paper":
        if computer == "scissors":
            return "Player wins"
        else:
            return "You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Player wins"
        else:
            return "You lose"

choices = get_choices ()
print(choices)
result = check_win (choices["player"], choices["computer"])
print (result)
