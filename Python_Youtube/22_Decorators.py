# ========== Decorators ==========

print( "Decorators")

## ======= Decorators Overview =========
    # Defined with @ symbol followed by the decorator name just before the function definition
    # Decorators are a way to change, enhance or alter how a function works in python 

# For Example, have a function called Hello: 
def Hello():
    print("Hello!")

# To add a decorator to the above do the following: 
# @logtime                                            # Function now has the log time decorator assigned
def hello():                                        # Therefore whenever we call the hello function, the decorator is going to be called
    print("Hello!")
    # The above on it's own won't return anything -> you'll get an error in the command window as follows:
        # Because log time as a function needs to be defined
        # Error in Terminal: NameError: name 'logtime' is not defined

# A decorator is a function that takes a function as a parameter, 
# wraps the function in an inner function that performs the job it has to do and returns that inner function

# For Example, another function defined as log time where we'll do something before and after the function
    # You want to use decorators to change the behaviour of a function without modifying the function itself
        # For example when you want to perform logging
        # Verify test performance 
        # perform caching
        # verify permissions etc etc etc

def logtime(func):                                  # Creat function called logtime function
    def wrapper():                                  
        print("before")                             # Print "Before" before the function runs
        val = func()
        print("after")                              # Print "After" after the function runs
    return wrapper
    # Return wrapper returns the before, the function hello() and the after function

@logtime                                            # Logtime defined above 
def hello():                                        # As before hello() function defined
    print("Hello!")

hello()                                             # Now we call the function 
                                                    # The command window returns 
                                                        # before
                                                        # Hello!
                                                        # after 
    # Running hello() allows you to run logtime above in conjunction allowing us to define the before and after commands to run
        # hello() function wrapped into inner function being "wrapper" which returns the inner function
        # logtime(func) returns wrapper which prints:
            # before
            # funct (which == Hello!) 
            # after 
        # into the command line
        # As you can see above the function wrapper returns the threee above with the return of the logtime(func) defined as wrapper


