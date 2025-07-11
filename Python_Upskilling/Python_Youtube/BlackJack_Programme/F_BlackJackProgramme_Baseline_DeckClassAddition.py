import random   # Import Random Python Module to access random.shuffle function

"""Suit, Rank and Cards Set Up"""

class Deck: 
    def __init__(self):
        self.cards = []                                              # New variable cards created with empty list assigned
        suits = ["Spades","Clubs","Hearts","Diamonds"]          # List of suits
        ranks = [                                               # List of ranks -> key value pairs
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

        """Random Card Generation for Dealer Dealing Cards"""

        for suit in suits:
            for rank in ranks:
                self.cards.append([suit,rank])                       # Append Suit and Rank to empty Card List above 

    """Create a Function to Shuffle and Deal a Card"""

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)                               # Now shuffle the cards using the random function
        else:
            print("Deck contains only 1 card") 

    def deal(self,number):                                       # number as input to the number of cards to be dealt
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
                return cards_dealt
            else:
                return print("No Cards in Deck")

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
    # Have done this above

# Note, a class is like a template, you can use that class to create an instance of that class called an object
    # each instance keeps track of its own state so you can update an instance created from a class and it won't impact other
    # objects created from the class
    # First lets prepare a class to make an instance from it
    # When you create an instance of a class, python automatically calls a function (Aka method) in the class named __init__
        # contents of __init__ method should be code that's run one time to initialise the instance

# Therefore at the beginning of our class lets create an init function
    # Remember from before always have to pass in self for all these functions in a class 
    # self is refering to the instance of the class we've developed

# Now indent all the code that's not part of the shuffle or deal function
    # Anything inside the paraenthesis is called an argument 
    # self represents the instance of the class
    # hence why self is the first item of the paraenthsis
        # add this to the first item of the parenthesis of the other functions

# Now the cards underlines as red -> before making shuffle and deal into a class we could just access this cards variable 
    # Now we cannot and need to fix this
    # Inside a class, in order to access a variable inside multiple functions (or methods), the variable has to start with self.
        # change all instances of cards in every function to self.cards
    # Self.cards in the deck class means we can access it in other places
        # Now this will be a variable that's immediately associated with the instance of the deck that's created
        # and we can access it in all of the other methods

# Now lets create the instance of a deck class
    # Make sure we're not indended at all and follow as appropriate
    # We can access cards from the instance of the class
    # As you would in normal blackjack now its time to make multiple deck classes to represent multiple packs of cards

Deck1 = Deck()
# Now create another instance of another Deck:
Deck2 = Deck()
# Notice how both Decks have not been shuffled
    # Deck Class inherits shuffle method
Deck1.shuffle
Deck2.shuffle
# Now lets add safe gaurds to prevent errors
    # Every time deal function is called - card is removed form cards list
    # You can only remove a card if there are cards to remove 
        # therefore need to safe gaurd against removing cards if the no. of cards in the deck = 0

    # Add condition in deal function to only allow pop if card number is > 
        # Added an if statement to describe this above
    # Now need to add a statement to only shuffle a deck if it has more than 1 card in it

    # Note, if statements do not need else statements coupled
        # We can add if statements where if the if condition is not met
        # we will do nothing 