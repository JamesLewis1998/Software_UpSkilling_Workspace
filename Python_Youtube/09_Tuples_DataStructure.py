# ========== Tuples ==========

print( "Tuples Data Structure")

## ======= Creating and checking against Tuples =========
# Allow you to create immutable data structure meaning it cannot be modified
# once created. Created in a similar way to lists but done using parenthasis
sports =("rugby","football","netball","basketball")

# Tuples are ordered like a list so can get a value like you would in a list via indexing
print(sports[0]) # "rugby"
print(sports.index("football")) # returns 1
print(len(sports)) # returns 4

# Can check if an item is in the tuple in the same way in which we would with lists
print("NFL" in sports) # will return false

# Return selection of values from Tuple using Indexing 
print(sports[0:2]) # returns ('rugby','football')
# remember return is up to index 2
# 0 is rugby 
# 1 is football

## ======= Modifying a Tuple =========
# Note as per description you cannot modify a tuple 
# So the following is a mechanism to sort and print a tuple 
print(sorted(sports))
# Here we're printing a sorted version of the tuple but does not modify the tuple itself 
print(sports)

## ======= Creating a New Tuple from an Existing One =========

sportsplus = sports +("NFL","Golf")
print(sportsplus)