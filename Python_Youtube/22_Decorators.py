# ========== Decorators ==========

print( "Decorators")

## ======= Decorators Overview =========
    # Defined with @ symbol followed by the decorator name just before the function definition
    # Decorators are a way to change, enhance or alter how a function works in python 

# For Example, have a function called Hello: 
def Hello():
    print("Hello!")

# To add a decorator to the above do the following: 
@logtime                                            # Function now has the log time decorator assigned
def hello():                                        # Therefore whenever we call the hello function, the decorator is going to be called
    print("Hello!")

# A decorator is a function that takes a function as a parameter, wraps the function in an inner function that performs the job it has to do and returns that inner function

# For Example, another function defined as log time where we'll do something before and after the function
    # You want to use decorators to change the behaviour of a function without modifying the function itself
        # For example when you want to perform logging
        # Verify test performance 
        # perform caching
        # verify permissions etc etc etc

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val 
    return wrapper

## ======= SUBTITLE2 =========





## ======= SUBTITLE3 =========




