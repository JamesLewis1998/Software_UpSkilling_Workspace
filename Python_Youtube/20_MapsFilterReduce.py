# ========== Maps Filter and Reduce Section ==========

print( "Maps Filter and Reduce Section")

# Python provides three useful global functions that we can use to work with collections
    # Maps 
    # Filter 
    # Reduce 

# Note since they're functions they're going to have the parentheses at the end, ie ()

## ======= Maps =========
    # Map is used to run a function upon each item in an iterable item like a list
    # And for example create a new list with the same number of items but each value against the item having being changed

# Example: 
numbers = [1,2,3]                   # Define a List:
def double(a):                      # Define a function
    return a*2                      # Function return

result = map(double,numbers)        # Now we run the double function on each item in the list via maps
                                    # Now we will get a new list

print(result)                       # returns the following in the command window
                                        # <map object at 0x0000025D245E9990>

print(list(result))                 # Pass into list function to obtain the output in the command field

    # The above can be used whenever you want to run a function on each item in a list

# Note when a function is a one liner like above, its common to do this as a lambda function

double = lambda a: a*2
result = map(double,numbers)
print(list(result))

# Can simply the above even more and this is where lamdba functions really shine: 

result = map(lambda a: a*2, numbers)
print(list(result))

    # The above is a very efficient way of refactoring code and optimising it
    # The result of all of the above is a mapped object which is iterable
        # That's why we needed to cast it to a list to print its content

## ======= Filter =========
    # Filter takes an iterable and returns a filter object
    # which is another iterable but without some of the original items

numbers = [1,2,3,4]                 # Define a list of numbers 

def isEven(n):                      # function defined as isEven
    return n % 2 == 0               # Check if the item passed in is even
                                    # When you divide by 2, and have a remainder of 0 - no. is even
                                        # in this instance the function returns as true
                                    # Note here the == operator confirms the true or false return
                                        # Remember = is assigning a value / variable
                                        # == is if the value is equal to the one define the result is true

result = filter(isEven, numbers)    # Pass in the filtering functon against the list
                                    # returning true or false from the isEven Function

print(list(result))                 # Here in the command window the values which are even are included in the output 
                                        # Values which are not even are ommitted from the output
                                        # The output will be [2, 4]

# As before we can simply the above using lamdba functions:

result = filter(lambda a: a % 2 == 0, numbers)
print(list(result))

## ======= Reduce =========
    # Reduce is used to calculate a value out of a sequence, like a list 

# For Example - have a list of expenses stored as tuples as follows: 
expenses = [            
    ('Dinner',80),                      # Remember tuples as a data structure is deonted by ()
    ('Car Repair',120)                  # Two tuples here - remember tuples are immutable
]
                                        # Long winded way of adding expenses up above 
sum = 0                                 # Defines sum as type int starting at 0
for expense in expenses:                # Using for and in to pick every expense from expenses 
    sum += expense[1]                   # then add to the sum where sum starts at 0
                                        # add expense [1] where 1 is the item at index 1 in the expense 
                                            # Ie ('Dinner',80) -> Dinner is at index 0 and 80 is at index 1
    # += equivalent to sum = sum + expense[1]
print(sum)                              # returns 200 in command window

# Reduce is a little different to Map and Filter - we have to import it from the standard library
    
    # function is contained within functools therefore use: 
from functools import reduce            # functools is one of the libraries

    # Taking the above example and re creating this as functions: 

# Define Expenses again:
expenses = [                            
    ('Dinner',80),                      # Defined in Tuples
    ('Car Repair',120)                  # Remember index [0] is Car Repair
]
sum = reduce(lambda a,b: a[1] + b[1], expenses)
    # Here lambda takes in two arguements 
        # First arguments is the accumulated argument
        # Second value is the update value from the iterable
    # Continue adding all of this together and reduce all the index values in the expense list into one number
        # The one number here being the total hence why it's referred to as "reduce"
    # Remember lamdba here in python is
        # A lot quicker to use the reduce function compared to the above code we have previously

print(sum)