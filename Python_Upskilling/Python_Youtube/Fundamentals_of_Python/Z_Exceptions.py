# ========== Exceptions Overview ==========

print( "Exceptions Overview")

## ======= Handling Errors =========
    # It's important to have a way to handle Errors and python gives
    # you exception handling to do so

# For exceptions handling you wrap lines of code in a try block
    # Inside the block you put the lines of code
    # Then if an error occures, python will inform you on which type of error has 
    # occured using an except block

try:                            # Followed by defined code 
    # some lines of code
except <ERROR1>:                # Followed by how to handle ERROR1
    # handler <ERROR1>
except <ERROR2>:                # Followed by how to handle ERROR2
    # handler <ERROR2>

# You can also catch all exceptions using an except without an error type
    # So at the very end you just do except where if you don't have an ERROR type 
    # it's just going to handle the rest of the exceptions

    # This would look as follows: 

try:                    
    # some lines of code
except <ERROR1>:                # Note here you would actually have to put an Error in the spot where ,ERROR1 is
    # handler <ERROR1>
except <ERROR2>:        
    # handler <ERROR2>
except 

## ======= Adding else into Exceptions =========
    # Note, you can add the following in at the end of this instead: 

try:                    
    # some lines of code
except <ERROR1>:        
    # handler <ERROR1>
except <ERROR2>:        
    # handler <ERROR2>
else:
    # else is here to run if there are no exceptions found
        # So if there are no errors in the lines of code
        # we can have an else as follows and run the specific code at the bottom
        # that runs if there are no errors

## ======= Adding in a Finally Block =========
    # Adding a Finally Block as follows: 

try:                    
    # some lines of code
except <ERROR1>:        
    # handler <ERROR1>
except <ERROR2>:        
    # handler <ERROR2>
else:
    # no exceptions were raised, the code ran successfully 
finally: 
    # do something in any case 

    # The finally block exists to always run something at the end
    # regardless of whether or not there were any exceptions or not
        # Ie the code in the finally block is always going to run

# Note, the specific error you get comes down to the code you're trying to run
    # For Example if you're reading a file you might get
        # E0FError which means end of file
    # If you divide a number by 0 you get a zero division error 
    # If you have a type conversion issue you might get a type error