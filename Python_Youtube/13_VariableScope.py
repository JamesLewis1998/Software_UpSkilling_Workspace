# ========== Variable Scope ==========

print( "Variable Scope")

## ======= Declaring Variables =========
# When you declare a variable that variable is visible in parts of your programme depending on where you declare it
# If you declare a variable outside of a function, the variable is visible to any code running after the declaration including functions
    # This kind of variable is known as a global variable 

# For Example: 
age = 8             # age is now a global variable as its declared outside of all functions 
def test():         
    print(age)      # print(age is the body of this function and the function test() output 

print(age)          # output in the command terminal is 8 because age is a global variable 
test()              # Running test prints the age in the command window because internal to the function there is a command to print age in the functions body 

# A function declared inside the function becomes a local variable
def test1():
    age1 = 10
    print(age1)

# print(age1) will return an error in the command window/ terminal because age1 is defined inside the function test1 and not declared globally
print(test1())      # Will return an output of 10 in the command terminal because the body of test1 has age1 declared internally to the function

## ======= Nested Functions =========
# Functions in python can be nested inside other function
# A Function inside another Function is visible only inside that function 
# Useful to create utilities that are useful to a function but not useful outside of it 

# Why hide a function if it does not harm? 
    # Always best to hide functionality that is not useful elsewhere
    # Also enables us to make use of closures

# For Example: 





## ======= SUBTITLE3 =========