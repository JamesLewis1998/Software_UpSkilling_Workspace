## ======= Python Package -> argparse =========
    # Above method is very work intensive:
        # Need to validate arguments 
        # Make sure type is correct 
        # Print Feedback to user if not using programme correctly

import argparse                                                     # Import argparse via usual method
parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'           # Description of the Programme
)                                                                   # Then proceed to add in arguments you want to accept
                                                                    # The argparse module allows you to specify custom type converters for your command-line arguments

parser.add_argument('-c', '--colour', metavar='colour',required=True, choices= {'red','blue'}, help='the colour to search for')
                                                                    # Here we accept a -c option or a --colour 
                                                                    # Additional fields can also be added such as choices above which will be described below
                                                                    # Specify whether it is required and what help is going to go along with it
args = parser.parse_args()
print(args.colour)                                                  # To get the colour that was passed in

# So now if we pass in the following onto the command line:
    # python Python_Youtube/18_ArgsFromTheCmdLine_SectionB.py -c blue
        # The inputs here being -c and the colour itself (blue)

# Note if you run the above without the arguments and just run: python Python_Youtube/18_ArgsFromTheCmdLine_SectionB.py
    # You will get the following error back: the following arguments are required: -c/--colour
    # Telling us we've called the programme wrong and are missing the required arguments

# We can define a specific set of inputs for the argument
    # argeparse makes it easier to communicate information back to the user 
    # it also makes it just easier to deal with arguments

# For example: 
# Adding the field choices = {"red","blue"} into the add_argument above
# if the following is inputted on the command line: python Python_Youtube/18_ArgsFromTheCmdLine_SectionB.py -c yellow
    # The return in the command line is the following: invalid choice: 'yellow' (choose from 'blue', 'red')
    # Because the only options or inputs available is blue or red -> yellow is not a valid input
    # The feedback such as invalid choice is a good way to feedback to the user to understand why arguments aren't valid