# ========== User Input ==========

print( "User Input Examples")

## ======= Simplifying Code =========

print("What is your age?")
age = input()
print("Your age is "+ age)
# We can simply this to group age and print functions
age = input("What is your age? ")
print("Your age is "+ age)

# Note, getting input when the programme is run is much better
# for command line applications

## ======= Control Statements =========
# Like an if statement, if condition is true, the function runs everthing 
# in the block - block is one level within a function, contents of block is 
# all lines of code that are indented the same amount 
# block ends whenever you move back to the previous indentation level

Condition = True
if Condition == True:
    print("the condition was true")
else:
    print("the condition was false")
print("outside if statement")

## ======= Series Returns for User Input =========

Age = 26 
Name = "James"
EducationLvl = "Masters"

if Name == "Ben":
    print("Surname is Dickinson")
elif EducationLvl == "Secondary School":
    print("Lower Education")
elif EducationLvl == "A Level":
    print("Mid Lvl Education")
elif EducationLvl == "Masters":
    print("Higher Lvl Education")
else:
    print("Uneducated")

# if condition == true, prints statement
# elif condition == true, prints that statement
# if anf elif conditions are all false, prints else statement 
