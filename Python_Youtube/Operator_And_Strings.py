# ==================== Operators ====================
# Assignment operator is used to assign a variable to a value 
# or a variable value to another varaible 
# Arithmatic Operators: Used to complete mathmatics 
Addition = 1 + 1
Subtraction = 2 - 1
Multiply = 2 * 2
Divide = 4/2
Remainder = 4 % 3 ; print (Remainder)
Powers = 4 ** 2 ; print (Powers)
Floor_Division = 5 // 2 ; print(Floor_Division)     # Rounds down division to the nearest integer

# Arithmatic Operators Combined with Assignment Operators 
age = 8 
age += 8 # This actually = age + 8 
print (age) 

# We can do this with any of these arithmatic operators 
# For example 

age1 = 8
age1 *= 8 # This means taking the age and multiplying it by 8 
          # I.e age*8 
print(age1)

# Comparison Operators 
a = 1 
b = 2

a == b # Double equals to compare if two values are equal to one another 
a != b # Compare if two values do not equal one another 
a > b  # Is a greater than b 
a <= b # Is a smaller than or equal to b 

# Note True and False are examples of the boolean data type meaning false or true

# Boolean Operators 
Condition1 = True 
Condition2 = False 

not Condition1              # Not means condition1 is not true - therefore not condition1 would return false because condition1 is true 
Condition1 and Condition2   # Means both conditions have to be true - would return false
Condition1 or Condition2    # Mean either condition has to be true - would return true

# AND & OR with Boolean  
# or and the use of python - if x is false then y, else x 
# if x is false then x, else y 

print(0 or 1) # returns 1 because 0 is false 
print('hi' or 'hey') # returns 'hi' because 'hi' is not false 
print([] or False)   # returns false because empty brackets is false and if x = [], then return y which = False
print(False or [])   # in this condition, x = False, therefore y which = []

print(0 and 1) # Returns 0 because x is false
print(1 and 0) # Returns 0 because x is true 
print(False and "hey") # Returns False because x is False
print('hi' and 'hey') # Reutrns 'hey' because 'hi' is not False 
print([] and False) # Returns [] because x is [] which is False

# Bitwise Operators
x = Condition1 & Condition2  # performs binary AND 
print (x) # returns false because condition1 and condition2 are both not true
# | performs binary OR 
# ^ performs a binary XOR Operation
# ~ performs a binary NOT operation
y = Condition1 | Condition2
print(y) # y Returns true because one of the two conditions are true
# >> shift right operation 
# << shift left operation

# Is and In Operator 

# Is is called the indentiy operator: used to compare two objects and returns true if both are the same object
# In is called the membership operator: used to determine if a value is contained in a list or another sequence

# Ternary Operator in Python