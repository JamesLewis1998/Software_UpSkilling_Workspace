# ========== The With Statement ==========

print( "With Statement")

## ======= Using With Statement to Open Files =========
    # With Statement is very helpful when working with exception handling
    # Each time we open a file we must remember to close it
        # With makes this process much more transparent

# If we're going to be working with files in python we do the following: 
filename = r'C:\Users\jdickin2\Documents\Software_UpSkilling_Workspace/requirements.txt'
    # Note without the r in the filename above you get the following error
        # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
    # Adding the r in:
        # Utilize raw strings by prefixing string literals with 'r', 
        # which treats backslashes as literal characters and prevents Python from interpreting them as escape sequences
    # Escape Sequences are:
        # An escape sequence is a sequence of characters that, when used inside a character or string, 
        # does not represent itself but is converted into another character or series of characters

try:
    file = open(filename, 'r')          # We open the file
    content = file.read()               # We read the file 
    print(content)                      # We then print the content of the file
finally:
    file.close()                        # Always close the file at the end
    
    # The above prints the content of the requirements file into the command window

# Doing the above using With Statement:
with open(filename, 'r') as file:
    content = file.read()
    print(content)
    # r in the open(filename,'r') simply defines the encoding: to make sure you read the file in correct encoding format.