import random   # Import Random Python Module to access random.shuffle function

"""Card Class"""
class Card:
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank'] } of {self.suit}"

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
                self.cards.append(Card(suit, rank))          # Append Suit and Rank to empty Card List above 

    """Create a Function to Shuffle and Deal a Card"""
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)                      # Now shuffle the cards using the random function

    def deal(self, number):                                  # number as input to the number of cards to be dealt
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

"""Hand Class"""
# Create Hand Class:
    # This will represent a hand class in the game of blackjack 
    # add an init class and within it initialise a variable called self.cards to an empty list
        # also make the hand keep track of the value of the hand so add this init __init__ and start it at 0

class Hand():
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value (self):
        self.value = 0
        has_Ace = False

        for card in self.cards: 
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "ACE":
                has_Ace = True

        if has_Ace and self.value > 21: 
            self.value -= 10

    def get_value(self): 
        self.calculate_value()
        return self.value

    def is_black_jack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and \
            not show_all_dealer_cards and not self.is_black_jack:
                print("dealer hand - hidden")
            if self.dealer == False: 
                print(card)
        
        if not self.dealer: 
            print("Value", self.get_value())
        print()

# In the BlackJack game there will be a Human controlled Hand and a Dealer controlled Hand
    
    # In init constructor method of the hand class create a dealer parameter
        # this is then set ot true or false to keep track of what type of hand it is
    
    # pass in parameter -> dealer
        # then just need to create a variable called dealer and set it to dealer
    
    # Remember from before function parameters can add default values
        # We want to make it so the default parameter of dealer is set to false
        # Remember we can define this in the parenthesis -> then its allocated false by default if nothing is specified

# Now a hand can be created so lets add some functionality: 
    # Add am Add card method -> this should take a card list as a parameter
    # Now add card list to the cards and use extend function to add this to the cards

# Lets create a set of tests to see what we have so far
    # Create a Deck
deck = Deck()
deck.shuffle()
    # Create a Hand
hand = Hand()
hand.add_card(deck.deal(2))
    # Print hand:
print(hand.cards)
    # When running this hand the following is produced in the command window: 
        # [<__main__.Card object at 0x0000017D61942050>]
            # Because in print cards above you're printing a list not an individual card

    # Try printing the first value in the cards list:
print(hand.cards[0])
    # Command window now returns card like so
        # ACE of Diamondss
print(hand.cards[0])
print(hand.cards[0],hand.cards[1])
print(hand.value)

# Now lets create something to calculate the value of the hand of cards dealt
    # inside the method we'll set self.value to 0
    
    # We also need to accomodate the fact that ACE can have the value of 1 or 11 depending on player choice
    
    # Add this to the top of the function to establish this if condition before calculating values
        # Note because we're only using has_ace internal to this function we do not need to add self.Has_Ace as it does not need to be visible outside this function
        # Then when going through a list of the cards check if it has an ACE
            # If it does, set has_Ace = true
    
    # Now if there is an ACE in the Deck and the persons value goes above 21, we want to set the ACE value to 1 as you would in a normal game of Black Jack
        # Extracting all this out for the if loop
            # If has_Ace and self.value >21:
                # Ie if has_Ace is true (above is short hand) and the value of the hand is above 21
                # then minus 10 from the self.value to change ACE value from 11 to 1

# Now let's get the value from the calculation function creating another method called get_value 
    # Notice how in get_Value you use self.calculate to call on this method to then return the value from it
        # shorthand version of this in the print statement being hand.value
            # self refers to the hand instance we're working with

# Create another method which returns true if there's a blackjack and false otherwise in hand class
    # return self.get_value == 21 -> if this is true returns True for is_blackjack

# Now finally create another function which returns/ prints the hand in the display

    # should either say dealers hand or your hand depending on whether self.dealer == true or false
    # User ternary operator to see whether its the dealers hand or your hand

    # My version:
        # if self.dealer == False:
        #    print(f"Your hand: {self.value}")
        # else:
        #    print(f"Dealer Hand: {self.value}")
    # Computer Version:
        # print(f'''{"Dealer's" if self.dealer else "Your"}hand:''')
            # triple quotes means you can have double quotes or single quotes inside the f string

   # Now add a for loop that will print out each of the cards in the function/ method
   # Now test this out by printing hand.display for your hand

print(hand.display())

# To view the dealers hand you can run the following
hand.dealer = True
print(hand.display())

    # In a real deal of blackjack you owuld never be able to see the dealer hand 
    # we therefore need to prevent this being visible in the command terminal
        # In order to do this we need to gain access to the card index - to determine if its a dealer or player hand
            # therefore need to update for loop to get access to both the card and the card index
        # for index, card in enumerate(self.cards):
            # if index == 0 and self.dealer
        # Developed this because cards are dealt to dealer first then player 
            # indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number

# However at the end of the game we will want to expose both the dealers and players hand to show the cards each have: 
    # therefore need to implement something to enable this
    # to do this create a new parameter in the display method called, show_all_dealer_cards and set to false
    # hide if we're not showing all the dealer cards hence
        # "not show_all_dealer_cards"

# Also if there's a blackjack, the game is over, the person with this is just going to win
    # in this instance we just print all the cards
    # you end up with quite a long line of code -> use backslash to move half of it to the next line