## ===== Zero Type Error Example =====
    # Try division by zero to visualise error: 
# result = 2/0
# print(result)
# The following is returned in the command window: 
    # ZeroDivisionError: division by zero
    # (because the result line of code has caused an error)

# Now try adding the operation within a Try Block: 

try:                    
    result = 2 / 0                  # Code we intend to write
except ZeroDivisionError:           # expected error for zero division
   print("Cannot Divide by Zero")   # What to return in command window when this error occures
finally:
    result = 1                      # Regardless of the result return 1 in the command window
print(result) #1

# This try block above allows you to recover gracefully and move on with the programme

## ===== Raising Exceptions in your own Programming =====

# You can raise exceptions in your own programme/ code too by using the raise statement
    # For Example by doing the following:
# raise Exception('An Error!')
    # You'll see the following in the command window
        # Exception: An Error!

# We can also integrate the above into the try block as follows: 
try:
    raise Exception('An Error!')    # Raise Exception
except Exception as error:          # Define exception as error
    print(error)                    # We get the following in the command window
                                        # An Error!
                                        # Because we've defined Exception above as error


## ===== Defining your own Exception Class =====
    # This extends from exception

class DogNotFoundException(Exception):  # Raise the Exception Error above into the class error
    pass                            # Pass here just means do nothing 
                                        # We use this when we define a class without methods or a function without code

# Now try this out: 
try:
    raise DogNotFoundException()
except DogNotFoundException: 
    print('Dog Not Found')
    # Prints the above in the command line because it raises DogNotFoundException from try above

# Can extend the above to give more context in the code: 

class DogNotFoundException2(Exception):
    print('Dog Not Found 2')
    pass

try:
    raise DogNotFoundException2()       # Raise the error in the class
except DogNotFoundException2:
    print('Dog Not Found Exception 3')