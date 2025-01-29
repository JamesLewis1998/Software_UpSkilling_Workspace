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
    
# = means assign operator 
# string is a word or set of variables around it
# whenever reference player_choice, code automatically replaces rock

# note indentation is important - any line of code indented same amount is 
# considered to be in that function
# return indicates whats returned when function get_choices is called 

# EXAMPLE ONE: GREETING TO CONSOLE
#   def greeting (): 
#       return "hi"
#   response = greeting ()
#   print (response)
# note in python you do not need to put anything at the end of each line 
# print response returns to console

# Dictionaires - in python they are used to store data values in key value pairs
# Example below -curly braces begining and end with key value pairs separated by comas 
# dict = {"name": "beau", "colour" : "blue"}
# Key is name and colour, value is beau and blue 
# value can be a variable eg could set to choices 
# surround by quotation marks its a string
# In example above can define dictionary name by typing name instead of dict and 
# adding curly brackets in

# Inputs are used to define inputs from the user to get inputs from them 
# whatever the person enters in this field gets saved against the variable in
# programme
# Python libraries are a set of useful functions so you don't have to learn 
# how to write python from scratch
# with basic pyhton its hard to get a programme to do something randomly
# import statements used to import libraries and usually put at top of programme

# list in pyhton used to store multiple items in a single variable
# Brackets are important in programming to ilsturate what the functions pruporse is
#    food = ["pizza", "burger", "pasta"]
#    dinner =random.choice(food)
#    print (dinner)

# functions can recieve arguments when they are called, data are called arguments
# can put things in parenthesis to enable function to pass data via new variables 
# if statement will allow a function to do different things depending on certain 
# conditions - see indetentations to understand contents of if statements

# EQUAL SIGNS
# Single equal sign is assignment operator
# double equal sign checks if two values are equal 

# indentation helps with containing return statmeents within if statements 
# contained within functions

# concatenate strings - means link strings together in a chain or series
# means you can combine strings with other strings or variables
# One Example of Combining strings and variables together
    # print("You chose" + player + "computer chose" + computer)
# quite often in programming there's multiple ways to do the same thing 
# another option is called f-strings 
# f-strings allows you to make strings with other variables and python code

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