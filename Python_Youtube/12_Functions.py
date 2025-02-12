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
    value["name"] = "Ben"

val1 = {"name":"James"}
change1(val1)
print(val1)


## ======= SUBTITLE3 =========




