# ========== Operator Overloading ==========

print( "Operator Overloading")

## ======= Operator Overloading Introduction =========
    # Operator overloading -> advancec technique comparable and use them with python operators 

# Take the following Dog class as an example:
class Dog:
    """The Dog Class"""
    def __init__(self, name, age):
        self. name = name
        self. age = age

# Now do two dog objects: 

Roger = Dog("Roger", 8)
Syd = Dog("Syd", 10)

# Use operator overloading to add a custom way to compare the two objects above based on the age property: 
    # Take the above and modify it as follows: 

class Dog:
    """The Dog Class"""
    def __init__(self, name, age):
        self. name = name
        self. age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

Roger = Dog("Roger", 8)
Syd = Dog("Syd", 10)

# Function __gt__ above used to compare the two objects to figure out whether one dog object age is > than the other
    # Ie. the function returns as True if the age is > than the other age (ie the thing you're comparing it to)
    # else it returns false
    # the gt in this means greater than

# Now run the following in the command window to determine whether the instance above is true or false

print(Roger>Syd)    # Will return false in the command window because Roger is < Syd

# Note the same way we've defined gt above, we can also define methods for:
    # Less than 
    # lower or equal to
    # greater than or equal to
    # not equal

# Can also create methods to go with different arithmetic operators so we can do the following: 

    # __add__() respond to the + operator
    # __sub__() respond to the - operator
    # __mul__() respond to the * operator
    # __turediv__() respond to the / operator
    # __floordiv__ respond to the // operator
    # __mod__() respond to the % operator
    # __pow__() respond to the ** operator
    # __rshift__() respond to the >> operator
    # __lshift__() respond to the << operator