# ========== Modules ==========

print( "Modules")

## ======= Modules Overview =========
    # Every python file is a module
    # You can import a module from other files 
        # This is the base of any programme with a degree of complexity
        # Promotes a sensible organisation and code re-use
        # Also how you create a piece of software with multiple python programmes
        # running in the same piece of software

# In a typical python programme 
    # One File acts as an entry point and other files are modules
    # these files expose functions that we can call from other files

# For example lets say we want to import the bark function defined in line 123 of 12_Functions.py
    # A module name is like any other symbol in Python. It must start with a
    # letter (one of a hundred thousand or so), and have only letters or
    # digits within it. Plus underscore, and maybe a couple more special
    # characters.
    # If you HAVE to have a strange name, try using the __import__() function.

# Change from using the 12_Functions to a new file defined for the Purposes of this Task
import Common_Functions
Common_Functions.bark()         # Will print woof in the command window
                                # This strategy allows us to load everything defined in a file

# Can also use the from import syntax to call function directly
from Common_Functions import bark
bark()                          # This strategy allows us to call specific functions from a file
                                # Allows us to just import the things we need 

## ======= Importing Dependencies on Location of File and File System =========
    # Importing of files depends on the location of the file and the type of file system
    # For Example Lets say we create a Subfolder within the Python_Youtube Area: 
        # Call this Subfolder Function Library - note most people would call this "lib" for short
        # Create file in folder called Animals.py
        # Then need to create an empty folder called __init__.py

# __init__.py is very important -> this tells python that the folder contains modules
from Function_Library import Animals    # From the Folder import the Animals File 
Animals.bark()                          # From this Animals subfolder 
Animals.tweet()                         # Function imported from Animals subfolder
Animals.moo()                           # Function imported from Animals subfolder 

# Or in order to import from a specific function within the file in the subfolder you can do the following
from Function_Library.Animals import bark
bark()                                  # This imports the bark function directly which can then be directly called on the 
                                        # command line

## ======= Python Standard Library =========
    # Python has a lot of prebuilt modules you can expose through the standard library
    # Standard Library is a large library of various utilities ranging from math utilities to debugging to creating graphical user interfaces

# Taking a look at the most common ones: 
    # 1. math for math utilities 
    # 2. re for regular expressions
    # 3. json to work with json
    # 4. datetime to work with dates 
    # 5. splite3 to use SQLite 
    # 6. os for Operating System Utilities 
    # 7. random for random number generation
    # 8. statistics for statistics utilities
    # 9. requests to perform HTTP network requests 
    # 10. http to create HTTP servers
    # 11. urllib to manage URLs 

# Can import the above modules that allow you to get extra functionality

## ===== Import Math Common Function =====

# Import the overall library:
import math
Ans = math.sqrt(4)
print(Ans)

# Importing section or Function within the Library: 
from math import sqrt
print(sqrt(4))