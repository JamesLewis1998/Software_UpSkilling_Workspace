import random   # Import Random Python Module to access random.shuffle function

"""Suit, Rank and Cards Set Up"""

class Deck: 
    suits = ["Spades","Clubs","Hearts","Diamonds"]          # List of suits
    ranks = [                                                # List of ranks -> key value pairs
            {"rank": "2" , "value": 2},
            {"rank": "3" , "value": 3},
            {"rank": "4" , "value": 4},
            {"rank": "5" , "value": 5},
            {"rank": "6" , "value": 6},
            {"rank": "7" , "value": 7},
            {"rank": "8" , "value": 8},
            {"rank": "9" , "value": 9},
            {"rank": "10" , "value": 10},
            {"rank": "JACK" , "value": 10},
            {"rank": "QUEEN" , "value": 10},
            {"rank": "KING" , "value": 10},
            {"rank": "ACE" , "value": 11},
    ]
    cards = []                                              # New variable cards created with empty list assigned

    """Random Card Generation for Dealer Dealing Cards"""

    for suit in suits:
        for rank in ranks:
            cards.append([suit,rank])                       # Append Suit and Rank to empty Card List above 

    """Create a Function to Shuffle and Deal a Card"""

    def shuffle():
        random.shuffle(cards)                               # Now shuffle the cards using the random function

    def deal(number):                                       # number as input to the number of cards to be dealt
        cards_dealt = []
        for x in range(number):
            card = cards.pop()
            cards_dealt.append(card)
        return cards_dealt

    shuffle()
    card = deal(1) [0]                                      # Take the first card dealt and 
    print(card)                                             # print card from deal function

"""Deck Class"""

# Classes provide a way of bundling functionality and context together
    # object can contain a number of functions called methods
    # As well as data that's used by these functions (Called attributes)

# Use Classes to model 3 parts of the game
    # A card
    # A Deck 
    # A hand
#  First things first is to make a class called Deck and put everything written above into that class
    # Indent everything above into the class 
# Note, a class is like a template, you can use that class to create an instance of that class called an object
    # each instance keeps track of its own state so you can update an instance created from a class and it won't impact other
    # objects created from the class
    # First lets prepare a class to make an instance from it
    # When you create an instance of a class, python automatically calls a function (Aka method) in the class named __init__
        # contents of __init__ method should be code that's run one time to initialise the instance