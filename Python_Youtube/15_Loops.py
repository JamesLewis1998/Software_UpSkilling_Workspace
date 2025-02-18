# ========== LOOPS ==========

print( "Loops")

## ======= Loops Overview =========
    # Essential Part of programming, in pyhton we have 
        # While Loops 
        # For Loops

## ======= While Loop =========

# condition = True                    # Condition defined as True
# while condition == True:            # While Condition is True the following is evaluated
#     print ("The Condition is True") # When this is executed the body of the function will run indefinitely in the command window
                                    # Do not run this as the function will infinitely print this into the command window

# To Fix this from happening on the command line, define the following:

condition1 = True
while condition1 == True:           # Whilst Condition1 is True the following statement is printed
    print("The condition1 is True")
    condition1 = False              # Now the Loop runs once - in this case first iteration is run as condition1 is evaluated as true
                                    # Then following this in the body of the Loop the condition1 is then evaluated to False and the condition1 is 
                                    # Then evaluated as False and control goes to the next instruction in the loop - for which there isn't one in this case

# It's common to add an iteration to stop the Loop after some number of cycles
    # For Example here's a While Loop with a Counter: 

count = 0                           # Count starts at 0 
while count < 10:                   # Whilst count is below 10, execute the following
    print("The condition is True")  # Print in the command window
    count = count + 1               # Increments the counter every time until we get to the end
                                    # count outside is initialisation value almost -> count begins at 0
                                    # count internal to while function then runs through 1-10 internal to function
                                    # Until count == 10 then the while Loop is exited and we move to:
print ("After the Loop")            # After count == 10 then code moves to this print condition and prints "After Loop in Cmd window"

## ======= While Loop Example =========

# For Loop Example:
    # We can tell python to execute a block a predetermined amount of times upfront without the need for a seaprate varaible and conditional to check its value 
    # Its commonly used to iterate the items in a list 

# Define a List: 
List = [1,2,3,4]                   # Item defined as list of 1,2,3,4
for item in List:                  # For each item in the list we're going to print the item
    print(item)                    # item is a way to refer to objects in a list

# Or we can iterate for a defined number of times using the range function as shown below
for item in range(15):              # Using the range function that return a list
    print(item)                     # Will return 0-14 in the command window
                                    # For the range, items are a way to refer to objects in that range

# Python provides several ways to iterate over list. The simplest and the most common way to iterate over a list
# is to use a for loop. This method allows us to access each element in the list directly.
    # Note you can use terms other than item: 
a = [1,2,3,4,5,6,7,8,9]
for val in a:                       # val is another way to reference elements in the list
    print(val)

## ======= Accessing Indexs of a List =========

# Accessing index of a list: 
values = [1,2,3,4,5,6]
for value in enumerate(values):     # This prints each item and the index of the item 
    print(value)                    # In command window this shoes as (0,1),(0,2),(0,3)
                                    # Where the first value is the index and the second is the value 

# Note in order to remove the brackets the following can be used: 
values = [1,2,3,4,5]
for index, value in enumerate(values): 
    print(index,value)              # Returns 0 1,1 2,2 3,3 4 etc in the command window

# The above can be applied with lists containing strings too: 
names= ["James", "Ben", "Sophie"]
for index, name in enumerate(names):
    print(index,name)               # Returns 0 James,1 Ben,2 Sophie

## ======= Break and Continue Summary =========
    # 