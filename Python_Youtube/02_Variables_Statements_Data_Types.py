# Creating Variables 
# Create new variable by asssigning (equal sign) a Value to a label
# Variable name can be composed of characters, numbers and underscores but cannot start with a number
# Examples: name1, name_james, HEIGHT
# if you create a new variable you should be assigning it to a value
# A python key word is something that is used to write python, things like
# for, if, elseif, def, while, import - all have very speicifc meanings in python 
# so cannot use them as a variable name
# key words turn blue in code to emphasis it being a key word

# Example
name = "James"
#Variable with string
age = 26 
#Variable with number

# Expressions and Statements in Python 
# An expression is any code that returns a value 
# A statement is an operation on a value 

# Example of a statement would be
print (name)
# Statement because it's doing something to the value

# Programme 
# A Programme is formed by a series of Statements
# Note can use semi colon to put multipel statements on single line 

name1 = "Ben"; age1 =24 ; print(name1)

# Comments 
# In python everything after hash mark is ignored
# Can also put inline comment

name2 = "Dean" #This is an inline comment 

# Indentation
# This is very meaningful in Python 
# Some other languages is not the case 
# Everything indented belongs to a block

# Data Types 
# Anything surrounded by quotation marks is a string 
# Can determine data type using type in code 

print (type(name)) #Outputs the Data Type in the Console 
print (type(name) == str) # True or False against type

# In Python, a class is a blueprint for creating objects, and an >instance is a realization of that blueprint
# For example: 

print(isinstance(name1,str))
# Above we are trying to see if name1 is an instance of a string
# int class = integer numbers 
# floating point numbers = fractions represented by float

print(isinstance(age,int))
print(isinstance(age,float))
# Checking to see if age is an instance of float

# Python automatically knows the data type from the value type in 
# programming, it knows "" = string, 1 = int and 1.5 = float

# Note you can reallocate data types outside of the normal allocation of 
# python. For example

age2 = float(60)
print(isinstance(age2, float))
# Here obviously 60 is an int but we've reallocated to float in python
# Can even do this to convert a string to an integer 

age3 = int("30")
age4 = 30
print(isinstance(age3,int))
print(isinstance(age4,int))
# age4 by default is int in python
# age3 has been reassigned to be int from string "30"

# Can take the above a step further to separate out in lines
# This is called casting, we are trying to extract an integer from this string below
# Note this only works if the string defined below is indeed a number, if the string was 
# set as a word the programme would fail/ you would get errors and bugs

print("Age is 25 as a string")
age5 = "25" 
number = int(age5)
print(isinstance(number,int))

# Other Common Types in Python
#   complex for complex numbers
#   bool for booleans 
#   list for lists 
#   tuple for tuples
#   range for ranges 
#   dict for dictionaries
#   set for sets