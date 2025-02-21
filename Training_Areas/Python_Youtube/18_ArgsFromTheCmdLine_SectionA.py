# ========== How to Accept Arguments from the Cmd Line in Python ==========

print( "How to Accept Arguments from the Cmd Line in Python")

## ======= Run a programme from Cmd line in VS Code =========
# Pressing the play button to Run a Python File is just one way of running the file on the Cmd Line 

print("hello")

# For Example, instead of pressing the play button to run this file and print Hello in the terminal you can run the following 
    # python Python_Youtube/18_ArgsFromTheCmdLine.py
    # python tells the Cmd line to run the python programme 
    # Then the name of the file is how this is called to run the programme 

# Note depending on whether you use python or python 3 (version 3 of python)
    # wILL dictate whether you use python or python 3 in the command line call above

## ======= Passing in Arguments via the Cmd Line =========
    # Basic way to handle arguements is to use the sys module from the standard library

import sys                                                          # Note, you would normally have all import statements on the first line
                                                                    # We're only calling it this far down because of running through examples
print(sys.argv)                                                     # This prints all the arguments inputted into the command window when running the following command 
                                                                    # python Python_Youtube/18_ArgsFromTheCmdLine.py James 26
                                                                        # James 26 are the two arguments passed into the command line when calling upon the function programme to be run

# Returns the following in the command line: 
    # ['Python_Youtube/18_ArgsFromTheCmdLine.py', 'James', '26']
    # I.e. Name of the File 
    # First input or argument of James
    # Second input or argument of 26 (note even though it's a number it comes in as a string)

# So taking the above we can use the following
name = sys.argv[1]                                                  # Here able to use the argument that's been passed in via the Cmd Line
print("Hello" + name)

# Now when we run the following on the command line: python Python_Youtube/18_ArgsFromTheCmdLine.py James 26
# The following is returned: 
    # ['Python_Youtube/18_ArgsFromTheCmdLine.py', 'James', '26']
    # HelloJames