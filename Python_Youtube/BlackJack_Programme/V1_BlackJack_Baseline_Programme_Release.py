import random   # Import Random Python Module to access random.shuffle function

class Card:
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank'] } of {self.suit}"

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

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))          # Append Suit and Rank to empty Card List above 


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
            else: 
                print(card)
        
        if not self.dealer: 
            print("Value", self.get_value())
        print()

"""Game Class"""

class Game():
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play?:"))
            except: 
                print("You Must Enter a Number")

        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
        
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["S","STAND"]:
                choice = input("Please choose HIT or STAND:").upper()
                print()
                while choice not in ["H","HIT", "S","STAND"]:
                    input("Please Enter HIT or STAND (or H/S)").upper()
                    print()
                if choice in ["HIT","H"]: 
                    player_hand.add_card(deck.deal(1))
                    player_hand.display
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
            dealer_hand.display(show_all_dealer_cards = True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand: {player_hand_value}") 
            print("Dealers Hand: {dealer_hand_value}")

            self.check_winner(player_hand,dealer_hand, True)
            
        print("\n Thanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted! Dealer Wins 🃏😢")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted! You Win 💥💸")
                return True
            elif player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
                print("Player an Dealer have Black Jack! Player and Dealer Tie! 🙄🥱")
                return True
            elif player_hand.get_value() == 21:
                print("Player has Black Jack! Player Wins! 🎴👏")
                return True
            elif dealer_hand.get_value() == 21:
                print("Dealer has Black Jack! Dealer Wins! 💩🧻")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("Player hand greater than Dealer hand! Player Wins!")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Player hand smaller than Dealer hand! Dealer Wins!")
            else:
                print("Player hand equal to Dealer hand! It's a tie!")
            return True              
        return False

g = Game()
g.play