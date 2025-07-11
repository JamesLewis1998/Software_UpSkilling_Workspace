import random   # Import Random Python Module to access random.shuffle function

"""Suit, Rank and Cards Set Up"""

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

"""Now lets update programme so we just print the value of the card"""

card_value = card[1].get("value")                       # Use get to access the value of the key value pair
print(card_value)
# Alternative approach: 
card_value = card[1]["value"]
print(card_value)
