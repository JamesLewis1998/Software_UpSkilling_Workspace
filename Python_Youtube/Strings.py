# ===== STRINGS =====

# String in python is a group of characters enclosed in "" or ''
'James'
"James"
name = "James" # Assign String to Variable 
 # Concatenate two strings using + operator 
fullname = 'James' 'Dickinson'
print (fullname)

# Can also apend to a string using a += operator 
full_name = 'James'+'Lewis'
print(full_name)
full_name += 'Dickinson'  #Adding Dickinson to James Lewis
print(full_name)

# Convert a number to a string using the str class constructor 
age =str(39)

# String can be multi line when assigned with a special syntax
# Multi-line string example:

print("""James is 

      26 

      years old     
""") # can use single quote in the same way 

print('''James
      
      works at
      
      JLR''')

# ===== String Built in Methods =====
print("James".upper()) # prints James in all caps 
print("james dickinson".title()) # Makes first letter of each string a capital letter

# Can also check things in the terminal
print("james".islower()) # returns whether the string is all lower cause - prints true if so 

# ==== Common String Methods =====

# isalpha() - checks if the string contains only characters and is not empty 
# isalnum() - checks if the string contains characters or digits and is not empty
# isdecimal() - to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower to check if a string is lower case 
# same above for upper 
# title() to get a capatilised version of a string 
# startswith() to check if a string starts with a speciifc substring
print("James".startswith("J")) # would return true 
# endswith() to check if a string ends with a specifc value 
# replace is to replace part of a string 
print("JamesXDickinson".replace("X","Lewis"))
# split() - to split a string on a specific character operator 
# strip() - to trim the whitespace from a string
print("JamesXDickinson".split())
txt = "     welcome to the jungle        "
print(txt)
x = txt.split()
print(x)
y = txt.strip()
print(y)
# join() to append new letters to a string
myTuple = ("James", "Lewis", "Dickinson")
a = "#".join(myTuple)
print(a) # result is James#Lewis#Dickinson
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.

# find() to find the position of a substring 
txt = "Hello, welcome to my world."
print (txt)                 # note you can realocate variables as we hve done above with txt 
b = txt.find("welcome")
print(b) # returns -1 if value is not found but above it returns 7 because
         # it's 7 character spacings in from 0 (H = 1)

name = "James" 
print(name.lower())
print(name)
# Example above illustrates that they all return a modified string but do not alter the original string

# Can use some global functions with strings 
# for example len - stands for length 
print(len(name))
# then can use the in operator to check if a string contains a substring 
print("am" in name) # returns true because substring "am" is in string "James"

# ====== Escaping Characters =====