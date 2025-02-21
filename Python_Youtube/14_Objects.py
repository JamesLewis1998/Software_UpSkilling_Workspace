# ========== Objects ==========

print( "Objects")

## ======= Objects Overview =========
# Everything in Python is an Object, Lists, Tuples, Dictionaires - everything is an object
# Even values of basic primitive types are objects, integers, strings, floats etc

# Objects have attributes and methods 
# These can be accessed with the dot syntax 

# Example - define variable of type int 
age = 8         # Age now has access to the properties and methods defined for all int objects including real and imaginary numbers

# For Example Printing Real and Imaginary Numbers
print(age.real)             # Prints the real element of age (8)
print(age.imag)             # Prints the imaginary part of the number ( returns 0)
print(age.bit_length)       # Returns the number of bits necessary to represent this number in binary notation

# A variable holding a list has access to a different set of methods:
# For Example here is a list:
items = [1,2]

items.append(3)             # Adds 3 to the List 
items.pop                   # Remove and return the last added item which is the 3 in this case
    # Here the append and pop are methods
    # The methods available to an object depend on the type of value 

# Id global function provided by python lets you inspect the local in memory for a particular object 
# For Example:
print(id(items))            # Returns the following in the command line 2871102099328
                            # This is the location in memory

## ======= Mutable vs Immutable =========
    # Some objects in python are mutable whilst others are immutable
        # This depends on the object itself
        # If an object provides methods to change its content then its mutable else its immutable
        # Most objects in python are immutable

# For example, int is immutable - there are no methods to change its value 
    # If you increment a value for example below, python creates an entirely new value so age won't be the same value because you 
    # have to create a whole new one to re-assign it 

age = 8 
print(age)                  # Returns 8 in the command window
age = age + 1
print(age)                  # Returns 9 in the command window

# However for something like a dictionary it would actually be the same object you'd just be changing different parts of it 

## ======= SUBTITLE3 =========


