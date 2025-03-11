import random   # Import Random Python Module to access random.shuffle function

"""Card Class"""
class Card:
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank'] } of {self.suit}s"

"""Deck Class"""
class Deck: 
    def __init__(self):
        self.cards = []                                     # New variable cards created with empty list assigned
        suits = ["Spades","Clubs","Hearts","Diamonds"]      # List of suits
        ranks = [                                           # List of ranks -> key value pairs
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
                self.cards.append(Card(suit,rank))          # Append Suit and Rank to empty Card List above 

    """Create a Function to Shuffle and Deal a Card"""

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)                      # Now shuffle the cards using the random function
        else:
            print("Deck contains only 1 card") 

    def deal(self,number):                                  # number as input to the number of cards to be dealt
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
                return cards_dealt
            else:
                return print("No Cards in Deck")

Deck1 = Deck()
Deck2 = Deck()
Deck1.shuffle
Deck2.shuffle

