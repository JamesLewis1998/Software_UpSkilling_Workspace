# Now lets begin with representation of a full deck of Cards with Python code: 

import random

# List of suits: 
suits = ["Spades","Clubs","Hearts","Diamonds"]

# Now create a list of ranks: 
    # A
    # 2 - 10
    # J, Q, K 
ranks = ["ACE",2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING"]

# Now create new varaible called cards and assign an empty list to the variable
cards = []

# Now for each item in the suits and ranks list, there should be pairings between them to create a total of 52 cards
    # ranks = 13 items in list
    # suits = 4 items in list
    # 4*13 = 52
    # Let's work up to this 

# Firstly add multiple elements into the print statement below: 
    # Firstly try printing an Ace in every suit
# for suit in suits:              # Create a for loop which prints each suit in suits in command line
#    print([suit,ranks[0]])      # List with suit and rank at index 0

# Now lets print every rank within every suit
    # this can be done easily with a nested for loop
        # ie a for loop within a for loop
    # As shown:

for suit in suits:              # Loop that loops through suits
    for rank in ranks:          # Loop that loops through rank 
        print([suit,rank])          # Nested for loop prints all 52 cards in a two item lists

# An element in a list can be another list
    # Sooo instead of printing 52 two items lists, lets append lists to the empty card variable above

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

# Note need to make sure cards is not contained/ indended within the nested for loop above otherwise the prints statement
# runs for every iteration of the nested for loop
    # The result of this is print every appendage of the suit and rank to the cards list
        # Ie. the following is printed in the command window
            # first for loop -> cards = [['Spades', 'ACE']]
                # Second for loop -> cards = [['Spades', 'ACE'], ['Spades', 2]]
                    # Third for loop -> [['Spades', 'ACE'], ['Spades', 2], ['Spades', 3]]

# Hence why we move this out of the indentation and have it out of the for loops below: 
print(cards)

# The next step is assessing the cards in the cards list - you'll notice in the command line that all the cards are in order
    # So we need to now reshuffle them as you would with a normal cards deck: 
        # import the random module at the top of your code
            # See line 3
    # Random module contains a shuffle function which will be perfect for card shuffling
        # As follows -> call random.shuffle and inputs cards into this: 

random.shuffle(cards)
print(cards)

# After the cards are shuffled lets remove a single variable from the cards list -> similar to a dealer dealing a card
    # this can be done with the pop method
    # Lets therefore create another variable and pop off a card from the cards list

card = cards.pop()              # Remember pop removes the last item from the list and returns it
print(card)

# The above sets the basics for the rest of the programme and can be refactored as such as shown in the next file:
    # BlackJackProgramme_Setup_Refactoring