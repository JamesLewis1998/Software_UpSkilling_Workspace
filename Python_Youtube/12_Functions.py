# ========== Functions ==========

print( "Function")

## ======= Overview =========
# Allows you to create a set of instructions when needed

def hello ():        # Name of the Function 
    print("hello")  # Body of the Function - Everything after the function and indended one level to the right
                    # indentation as discussed is important 
                    # functions also promote code readability and reuse

# To call the function:
hello()             # write the name of the function then add ()
hello()             # () is the syntax in programming used to call the function
hello()             # You can call on the funcion as much as you want as demonstrated

# Now if you run this programme in the command window it will print hello 3 times 
# Name of the function should be descriptive so anyone calling it can imagine what the function does
# A Function can accept one or more parameters 
# If you type in a parameter, this becomes a varaible of the function 

def hello1(name):           # name is the variable of the function
    print('hello'+name)     # Now call the function by passing the arguement through into the function
hello1("James")
hello1("Ben")

# Side note, always use single quotes or double quotes, try to avoid mixing between the two in code to be consistent
# Parameters are values accepted by the function inside the function definition
    # So above the parameter is name 
# Whereas arguments are passed to the function when we call it
    # Arguemnts can have a default value which is applied if the arguement is not specified

# hello1() # If you call this function on its own you will get an error as follows: 
           # TypeError: hello1() missing 1 required positional argument: 'name'
           # However we can make this function run without the need to pass a name

# How to make the name input option in the above function
def hello2(name = "my friend"):           # name is the variable of the function
    print('hello'+name)                   # inserting the = operator means if you don't pass in the name 
                                          # the string "my friend" will be used by default 
hello2()                                  # Calling function without speicfying any argument or parameter

# Can also specify function with multiple arguments: 

def hello3(name = "ben",age = 24):
    print("My name is" + name, "and my age is " + str(age) + " years old")
    # Need to specify age as string to avoid the following error
    # TypeError: can only concatenate str (not "int") to str
    # Ie passing age in as a number but we've converted it to a string

hello3("James",26)
    # Parameters are passed by reference
    
## ======= Functions and Immutable objects =========
# All types in python are objects but some of them are immutable
        # Including integers, booleans, floats, strings and tuples
            # Therefore if you pass the parameters and modify them inside the function
            # the new value is not refelected outside the function 

def change(value):          
    value = 2               # Once its inside the function and we change it, it doesn't change anything 
val = 1                     # Outside the function
change(val)
print(val)                  # Output from this will be 1 because what we change inside the 
                            # function doesn't change or effect anything outside the function

# HOWEVER, if you pass an object that is not immutable, you do change one of the properties and the change will be 
# reflected outside the function
    # An object that would be mutable would be a dictionary 
    # mutable meaning it can be changed
# Dictionary Example: 

def change1(value):
    value["name"] = "Ben"   # Change the name to Ben using the change function because the dictionary is mutable

val1 = {"name":"James"}     # val1 in dictionary "name" is defined as "james"
change1(val1)               # but the value inside the function change is changed to "ben"
print(val1)                 # Because a dictionarys mutable
                            # Output from print is {'name': 'Ben'} in command terminal 
# value["name"] in the function body references the key of the dictionary 

## ======= Return Statement =========
# A function can return a value using the return command in the function statement
# Returns a value we can continue to use in our programme 
# For Example:

def change2(name): 
    print("Hello" + name + "!")   # Here the function returns the name which will continue to be used in the programme
    return name                   # When the function meets the return statement, the function ends
                                  # We can also omit the return value to finish the function and not return anything

def change3(name): 
    if not name: 
        return                    # This ends the function and we don't even need an else
    print("Hello" + name + "!")   # If there is a name the function will return the print statement

change3(False)                    # Means the function will action the return in the body
                                  # Because we have to define something as an input into the function 
                                  # Alternatively we could define the default as False 

def change4(name = False):        # Default set to false in the function input 
    if not name:                  # if not name, ie if name = False, return 
        return 
    print("Hello" + name + "!")   # else the function will print as shown in command window

change4("James")                # Outputs HelloJames! in the command terminal

# wE CAN TAKE THE ABOVE AND CONVERT TO THE FOLLOWING: 

def change5(name):
    print('Hello' + name + "!")  # This function prints this in the command window
    return name, "James", 26

print(change5("Ben"))           # This is then going to print what's returned by the function with the input "Ben"
                                # so this command runs the function change 5 with the input as "Ben"
                                # Meaning the output in the command window is:
                                # HelloBen!---> Print output in the body of the function change5
                                # ('Ben', 'James', 26) ---> return output in the function with "Ben", "James",26

