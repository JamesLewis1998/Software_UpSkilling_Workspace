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

def deal(number):
    cards_dealt = []
    for x in range(number):     
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()

# Create new variable called card and assign to the variable a single card to be dealt with from the deck and make sure the card is
# not in a list:
    # We want to get the card out of the list by reference the first item in the list that deal returns
    # deal(1) deals one card and references the first item in that whats being delt

card = deal(1) [0]
print(card)

"""Now lets Update the Ranks List"""
# Each element of the ranks list should now be a dictionary, when lists or list elements are long its common to put each one on
# its own line - put each element on its own line with each one having the rank and value
    # Rememebr a dictionary needs key value pairs using key: key_definition, value: value_Definition

# Each Element in the list below is a dictionary defining a key value pair btwn rank and value

rank = [
{"rank": 2,"value": 2}
{"rank": 3,"value": 3}
{"rank": 4,"value": 4}
{"rank": 5,"value": 5}
{"rank": 6,"value": 6}
{"rank": 7,"value": 7}
{"rank": 8,"value": 8}
{"rank": 9,"value": 9}
{"rank": 10,"value": 10}
{"rank": "JACK","value": 10}
{"rank": "QUEEN","value": 10}
{"rank": "KING","value": 10}
{"rank": "ACE","value": 11}
]

# Refactor the above to contain all of this in BlackJackProgramme_Baseline