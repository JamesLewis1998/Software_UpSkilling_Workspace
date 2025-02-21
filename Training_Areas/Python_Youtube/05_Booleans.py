# ========== BOOLEANS ==========

print( "Booleans Introduction")

## ======= If Conditions with Booleans =========

Done = True 
Done = False
print(Done) # Prints False because Programming is sequential

Done = True 
# Evaluating a value for true or false
# If body of if statement is true, then the condition returns true 


if Done:
    print("yes") # Returns yes if Done is True 
else: 
    print("no") # Returns no if Done is False
                # Using this in the context of numbers, numbers are always true 
                # exept for 0 which is false 

# If Done = 0 Returns False
# If Done = -10 Returns True
# If Done = 10 Returns True

# Strings are always true unless empty 
# If Done = "Done" Functions return true 
# If Done =  "" Functions return false

## ======= Check if value is a Boolean =========

print(type(Done) == bool) 

# if Done = "True" Function above returns false
# If Done = True Functiona above returns True
# If Done = 10 Function above returns false 

## ======= Any Function =========

book1_read = True
book2_read = False

readanybook = any([book1_read,book2_read])
# Functions defines if any book is read then return true
# Ie if any of the conditions in the any function are true
# the function returns true
print = (readanybook)

# All function is true but returns true if all conditions in 
# the function are defined as true 
readallbook = all([book2_read,book1_read])
# Therefore function will return false because book2 is false 




