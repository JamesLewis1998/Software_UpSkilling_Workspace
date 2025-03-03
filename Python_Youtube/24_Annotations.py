# ========== Annotations ==========

print( "Annotations")

## ======= Annotations Overview =========
    # Python is dynamically typed so we do not have to specify the type of a varaible or 
    # or function parameter or a function return value
    # Annotations allow us to optionally do this

# For example, a function without annotations:
def increment(n):               # Simple Increment Definition
    return n + 1                # Return is number + 1
print(increment(2))             # Returns 3 in the command window 

    # Lets say we want to take the above and make this function only accept an int
    # The following achieves this: 

def incrementAnn(n: int) -> int:   # Here the function is defined as recieving an int and returning an int
    return n + 1

# We can take the above and do the same with variables too
count = 0

    # Specify condition as follows: 

count: int = 0                  # Here w have specified this variable is going to be an integer 

# Now python will actually ignore these annotations
    # A separate tool called mypi can be run as stand alone or integrated with 
    # by ides to automatically check for type errors statically whilst you're coding 
        # Very helpful when you're software becomes large and you need to refactor your code