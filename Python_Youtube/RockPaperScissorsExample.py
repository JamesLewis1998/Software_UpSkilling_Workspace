# RockPaperScissors Programming Example
import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors:")
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
result = check_win (choices["player"], choices["computer"])
print (result)

# this is going to call check win with rock instead of player and paper instead 
# of computer 
# whenever reference player_choice, code automatically replaces rock



# else and elif statements - else if is a combination of if and else statements 
# elif - looks at the if conditions then move onto elif to consider if statement within
# else statement 
#    age = 20 
#    if age >= 18: 
#        print("adult")
#    elif age > 12:
#        print("teen")
#    elif age > 1:
#        print("child")
#    else:
#        print("baby") 
# can also check for two conditions at once 

# Refactoring is the process of resturcturing code whilst keeping original functionality 
# common to refactor code to make it simpler or more understandable @ a quick glance
# nested if statement makes code more understandable at a quick glance 
# can put an if inside another if elif or else statement

# note once you return something, the rest of the code in a function does not run 
# so where something is place is sequential to this return statement

# placement of indentations in programming matter - driving sequence of functions 
# and order of which they are executed in 