#RockPaperScissors Programming Example

import random
#Loads the random module, which contains a number of random number generation-related functions

# ----------------------------
# Need to define dictionary of potential outcomes for player and computer

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice rock, paper, scissors:")
    computer_choice = random.choice (options)
    choices = {"player": player_choice, "computer" : computer_choice}
    return choices

# get_choices is the Function above 
# input above is used for user to define RPS input in console
# name of input assigned to "player_choice"
# options defines a list of potential choices for player and computer 

# random.choice calls on the imported module to assign random variable to computer_choice
# based on the options variable 

# choices is defined as a dictionary comprising of key value pairs 
# the key is defined as player and computer with the value of player_choice
# and computer_choice respectively 
#---------------------------------
# Now need to define the rulesets underwhich computer or player wins 

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

# check_win is the function and the inputs are player and computer
# data are called arguements and the arguements this function receives
# are the player and computer inputs 

# Note Parenthesis () contains arguements of the function being player 
# and computer above

# F strings used above (concatenate string could also be used) to print
# You chose and Computer chose with the player and computer variables

# ----------------------
# Now we have functions defined above with ruleset of winning and inputs into
# programme we need to return the result in the command window

choices = get_choices ()
print(choices)
result = check_win (choices["player"], choices["computer"])
print (result)

# choices is allocated as output from get_choices function
# result is the output of the check_win function where the input to
# this function is choices of the player and the computer from the 
# get-choices output 
# remember player and computer are the keys and player_choice/ computer_choice 
# are the values associated to these keys