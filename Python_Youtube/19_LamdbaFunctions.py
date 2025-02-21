# ========== Lambda Functions ==========

print( "Lamdba Functions Overview")

## ======= Lamdba Function Overview =========
    # Lamdda functions aka anonymous functions are small functions that have no name 
    # and only have one expression as their body 

# Lamdba Functions defined using the Lamdba Key word 
    # See the following example: 

lambda num : num * 2
    # num (left) = the argument 
    # num (right) = the expression 
        # Note an expression returns a value, a statement does not
        # Here the value being returned is the number * 2
    # This is the simplest version of a lamdba function
        # This takes a number input and doubles it

# Note, the lamdba function can accept more arguments: 
    # For Example

lambda a,b : a*b
    # Lamdba Functions cannot be invoked directly but you can't assign them to
    # For instance we can assign the above to a variable called multiply

multiply = lambda a,b:a*b
    # Multiply is the variable
    # Lambda is the function
print(multiply(2,4))
    # The output in the terminal will be 8 where the inputs are shown in brackets above

# The utlility of lamdba functions comes when combined with other python functionality
    # For example in combination with map, filter and reduce