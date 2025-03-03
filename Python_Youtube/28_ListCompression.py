# ========== List Compression ==========

print( "List Compression Summary")

## ======= List Compression Overview =========
    # List Compressions are a way to create lists in a very concise way 

# For Example, create a list of numbers: 
numbers = [1,2,3,4,5]

# Now create a new list using list compressions composed by the numbers list elements to the power of 2:
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)          # Produces a list in command window of every number to the power of 2
                                # Note the syntax above is whats used to create list compressions
                                    # ie n**2 is the command to put the entry to the power of 2
                                    # for n in numbers is the way to generate the list

# Note, list compressions are a syntax that's sometimes preferred over loops as its more readable and the operation can be written on a single line

# This is how you do it in a loop
    # What you do in a single line above takes multiple lines to do the following: 

numbers_power_2_loop = []       # Define an empty list
for n in numbers:               # Define for loop entry condition -> for n 
    numbers_power_2_loop.append(n**2)
print(numbers_power_2_loop)

# This is how you would do it using map:

numbers_power_2_map = list(map(lambda n : n**2,numbers))
print(numbers_power_2_map)      # Remember
                                    # # Map is used to run a function upon each item in an iterable item like a list

# Again, both the loop and list approach above are more complex
    # It's simpler in both cases here to use the list compression syntax and makes for more efficient code/ programming