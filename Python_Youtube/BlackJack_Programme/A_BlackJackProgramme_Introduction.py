# First Thing to do is allocation of a suit, rank and value:
suits = ["Spades","Clubs","Hearts","Diamonds"]
suit = suits[2]                                         # Remember the index 0 is the first value in the list
rank = "K"
value = 10

print("Your card is " + rank + " of " + suit)           # String Concatenation here
                                                            # remember to add a + on both sides when concatentating strings

# Not part of Final code but lets say you wanted to add snakes to the suits list:
    # Option 1
        # Use the append function 
            # suits.append("snakes")
    # Option 2
        # Use the extend function
            # suits.extend("snakes")
    # Option 3
        # Use the += operator
            # suits += ["spades"]

for s in suits:                                         # Create a for loop which prints each suit in suits in command line
    print(s)

# Now move onto representing a full deck of cards using python code
    # Detailed in BlackJackProgramme.pyhton