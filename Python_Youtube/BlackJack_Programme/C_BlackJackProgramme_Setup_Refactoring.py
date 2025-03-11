# Now lets begin with representation of a full deck of Cards with Python code: 

import random   # Import Random Python Module to access random.shuffle function

"""Suit, Rank and Cards Set Up"""

# List of suits: 
suits = ["Spades","Clubs","Hearts","Diamonds"]
# Now create a list of ranks: 
ranks = ["ACE",2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING"]
# Now create new varaible called cards and assign an empty list to the variable
cards = []

"""Random Card Generation for Dealer Dealing Cards"""

# Now for each item in the suits and ranks list, there should be pairings between them to create a total of 52 cards
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])           # Use the append function to append lists of card pairings to empty cards list above

"""Create a Function to Shuffle and Deal a Card"""
def shuffle():
    random.shuffle(cards)                   # Now shuffle the cards using the random function
                                            # When shuffle function is called we therefore shuffle the cards

# Call upon Shuffle function in programme:
shuffle()
print(cards)                    # Print Cards to demonstrate shuffled deck in command window

# After the cards are shuffled lets remove a single variable from the cards list -> similar to a dealer dealing a card
def deal(number):
    cards_dealt = []
    for x in range(number):                         # x being a number in range
                                                        # We are now looping x number of times which is defined by the number
        card = cards.pop()                      # Remember pop removes the last item from the list and returns it
        cards_dealt.append(card)                # Pop the card out then append this to the cards_dealt list
                                                        # Loops through based on the number of times you want to deal cards
    return cards_dealt                                 # Print card in the command window to demonstrate the random card generation from the list
                                            # Remember variables can only be accessed in the context they were created
                                                # So as it stands the card variable cannot be accessed outside of the deal function
                                                # Hence why return statement is introduced to return the card

card_dealt = deal(2)                               # call the deal function and assign the returned variable to a variable named card: 
print(card_dealt)                                 # Print card in the command window 

# Now create another Function called deal and move the pop line within this deal function above

"""What about if you want to deal multiple cards"""
# Lets refactor the deal function above to accept an argument -> any number of arguments can exist inside the parenthesis when a function is created seaprated by commas
    # Inside the function the arguments are assigned to variables called parameters

# Start by making it so the deal function takes an argument named number 
    # add in "number" into the paraenthsis in the function
    # then when we call the function we'll make sure we use the new parameter by making it so we deal 2 cards
        # Note, this alone does not allow you to deal two parameters 
            # We need to add more detail into the function to enable such in the deal function
    # In the first line of the function create an empty list called cards dealt
        # Now look at using the range function with the for loop covered earlier in the course
        # Create a for loop that adds a card to the deck for each card dealt

# Now need to refactor the above code to print the first card created and dealt in the list:
print(card_dealt[0])                        # Now print the first card returned by indexing as 0

"""Separate out the Rank Variable"""
# Now lets create a variable named rank and assign it the rank from the card: 
rank = card_dealt[0][1]                         # [0] accesses the first variable in the card-dealt list 
                                                # [1] accesses the second item in the first varaible of the list
print(rank)

#Another way to contain this is to allocate card to [0]:
card = card_dealt[0]
rank = card[1]

"""Recognising Rank and value of Ranks in Suit Cards"""
# JACK, QUEEN and KING All have the value of 10 in the game
# ACE can be either 1 or 11 but we'll come onto this later 
# We therefore need to check what the rank is and set the value based on the rank
    # Perfect time for a conditional statement - maybe an if statement
    # depending on the outcome assign the result to a variable named value

# Remember the three logical operators
    # And, Or and Not
    # can use elif statements to loop through multiple conditions

if rank == "KING" or rank == "QUEEN" or rank == "JACK":
    value = 10
elif rank == "ACE":
    value = 11
else: 
    value = rank

    # Now lets print the rank and the value: 
    # Easily achieved using the following

rank_dict = {"rank":rank, "value" :value}       # Here we have the string rank here and the actual rank variable 
                                                # and the string value and the actual value variable
print(rank_dict)

print(rank,value)                               # When multiple values in an if statement are listed with a comma separating them
                                                # both values are printed with a space inbetween

"""Now lets talk about Dictionaries in Python"""
    # Like a list but more general - mapping between a set of indicies called "keys" and "values"
        # relating to key value pairs 
        # indicies in this context are called keys which have a value associated to it 

# So lets create a variable called rank_dict above print statement above and create a dictionary between two values
    # one being the value
    # the other being the rank
# Need a key value pair for the rank and a key value pair for the value

""" Refactor the code to get the value of each rank without using the if statement"""
# Instead, we'll store both the rank name and value in the ranks list using dictiionaries

# Delete all of the Lines after where it says shuffle and Refactor into
    # BlackJackProgramme_Baseline_Restructuring