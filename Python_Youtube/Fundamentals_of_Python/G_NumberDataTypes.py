# ========== Number Data Types ==========

print( "Number Data Types")

## ======= Complex Numbers =========
# Extension of a real number system  where all numbers are expressed as 
# a real part and imaginary part -> imaginary unit is the sqr rt of -1
# i in mathamtics and j in engineering 
# in prgramming we use j

num1 = 2 +3j 
# Or it can be represented as
num2 = complex(2,3)
# 2 = real part (integer)
# 3 is the imaginary part
print(num2.real) # 2.0 (returns float values)
print(num2.imag) # 3.0 (returns float values)

#Remember we can group this into one print request
print(num2.real, num2.imag) # returns 2.0 3.0

## ======= Built In Functions that Deal with Numbers =========

num3 = -5.5
abs(num3) # returns the absolute value of a number/ arguement
          # Magnitude of a number without considering a + or - sign
round(num3) # round to nearest integer
round(num3,1) # round to the nearest one Decimal Place 

## ======= Enums =========
# Readable names bound to a constant value 
# import enums from standard library module

from enum import Enum
# Once imported can initialise a new Enum via:
class state(Enum):
    INACTIVE = 0 
    ACTIVE = 1 
    # Setting a variable where state.inactive = 0 
    # and state.active = 1 
print(state.ACTIVE)
# Note A class is a code template for creating objects. 
# Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class

# Note print(state.ACTIVE) returns state.ACTIVE instead of 1 
# To actually get the value you need to use the following:
print(state.ACTIVE.value)

# Vice versa to achieve the same outcome:
print(state(1))
# Alternatively: 
print(state['ACTIVE'])

# This is essentially the only way to ceate a constant in python
# Python has no way to enforce a variable that should be a constant so 
# people use enums to create a constant and then no one can reassign the values

## ======= List all the values in a Class =========
print(list(state)) # Returns [<state.INACTIVE: 0>, <state.ACTIVE: 1>]
print(len(state)) # Returns the length of the state which wil equal 2