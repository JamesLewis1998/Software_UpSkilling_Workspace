# ========== Docstrings Overview ==========

print( "Docstrings Overview")

## ======= Docstrings =========
    # Documentation is very important to communicate the purpose of code and sections within to understand what sections
    # are supposed to do - one of the reasons ppl add comments
    # But another way to document purpose is use of doc strings

# For Example for a simple increment function: 
def increment(n): 
    """Increment a number"""        # the utility of a docstring is that it follows conventions
    return n + 1                    # so they can be processed automatically 
                                    # three quotation marks with purporse of this function within the quotation marks

## ======= Docstrings for a class and method =========
    # For example defining a class as follows:
class Dog: 
    """A class representing a dog"""# Defines what the class is
    def __init__(self, name,age):
        """Initilize a new dog"""   # Defines what the method does
        self.name = name 
        self.age = name
    
    def bark(self):
        """Let the dog bark"""
        print("WOOF!")

## ===== Common to put Docstring @ top of file =====
    # Docstrings can extend across multiple lines provded the lines start and end with the 3 quotations
    # As shown as follows: 

"""Dog module
This module does... bl bl bl and provides the following classes: 
- Dog
- Cat
"""
# note, python will process the docstrings and you can use the help global function to get the documentation for 
    # a class
    # a method
    # a function
    # a module

# For example:
print(help(Dog))                    # when you run this in the command window you get:

#   class Dog(builtins.object)
#   |  Dog(name, age)
#   |
#   |  A class representing a dog
#   |
#   |  Methods defined here:
#   |
#   |  __init__(self, name, age)
#   |      Initilize a new dog
#   |
#   |  bark(self)
#   |      Let the dog bark
#   |
#   |  ----------------------------------------------------------------------      
#   - More  --

# Pressing enter in the command window returns the following:

#   Data descriptors defined here:
#   |
#   |  __dict__
#   |      dictionary for instance variables
#   |
#   |  __weakref__
#   |      list of weak references to the object

#Docstrings are specific standards and makes it easier to get information using different helper methods
    # a lot of other methods to docstrings to allow someone to get information on the purpose of your code