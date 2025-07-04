import random   # Import Random Python Module to access random.shuffle function

"""Suit, Rank and Cards Set Up"""
class Card:
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank'] } of {self.suit}s"

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
                self.cards.append(Card(suit,rank))                       # Append Suit and Rank to empty Card List above 

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

Deck1 = Deck()
# Now create another instance of another Deck:
Deck2 = Deck()
# Notice how both Decks have not been shuffled
    # Deck Class inherits shuffle method
Deck1.shuffle
Deck2.shuffle

"""Card Class"""
# Lets create a card class with an init function we'll set self.suit to equal Hearts

# Refactor the code above so that a suit and rank is specified when a card object is constructed
    # init method can take additional arguments on top of self
    # Update to take in suit and rank

# Now create special method thats __str__ within card class
    # when a class has this specific method, it's called when print is invoked on an object
    # within a class
    # So when we print an object from the card class we want it to print something like 
        # "10 of Hearts"
        # print(self.rank + "of" + self.suit) -> this is the incorrect approach
    # Instead it should be approached in the following manner:
        # As before init used to define self with assignment of suit and rank within Class

# Now use the Class defined to create a card and print it into the command window:
Card1 = Card("Heart",{"rank": "ACE" , "value": 11})
print(Card1)
# You can see from here how we can use this to then create a Deck of 52 Cards

# Now refactor the following via the use of fstrings to simplify the code:
    # self.rank["rank"] + " of " + self.suit + "s"
    # f strings allow us to put variables right within a string
    # f "{self.rank["rank"]} of {self.suit["suit"]s"}
        # Note this will give an error because you have "" inside ""
            # to remedy this you need to change "" inside to ''
    # Currently in the Deck Class, the last line of the init method -ie for suit in suits: 
        # appends a list as an item to the cards list
        # instead of appending [suit, rank] lets create and append an instance of the card class
        # then afterwards when a deck is created its filled with cards
        # Replace with Card(suit,rank)
            # We're now passing in Card instances