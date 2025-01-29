# Workspace Overview

Repository to contain all work conducted within Fleetcode and Python Training.

## Key Learning Points from RPS Example

- = means assign operator 
- string is a word or set of variables around it

### Indentation 

1. note indentation is important - any line of code indented same amount is considered to be in that function

2. return indicates whats returned when function get_choices is called 

#### EXAMPLE ONE: GREETING TO CONSOLE

```
  def greeting (): 
       return "hi"
   response = greeting ()
   print (response)
```

- note in python you do not need to put anything at the end of each line 
- print response returns to console

### Dictionaries 
1. Dictionaires - in python they are used to store data values in key value pairs

#### Example

Example below -curly braces begining and end with key value pairs separated by comas 
 dict = {"name": "beau", "colour" : "blue"}
 Key is name and colour, value is beau and blue 
 value can be a variable eg could set to choices 
 surround by quotation marks its a string
 In example above can define dictionary name by typing name instead of dict and 
 adding curly brackets in

### Inputs 
 Inputs are used to define inputs from the user to get inputs from them 
whatever the person enters in this field gets saved against the variable in
 programme

### Python Libraries 

 Python libraries are a set of useful functions so you don't have to learn 
 how to write python from scratch
 with basic pyhton its hard to get a programme to do something randomly
 import statements used to import libraries and usually put at top of programme

### Lists

 list in pyhton used to store multiple items in a single variable
 Brackets are important in programming to ilsturate what the functions pruporse is
    food = ["pizza", "burger", "pasta"]
    dinner =random.choice(food)
    print (dinner)

### Functions

 functions can recieve arguments when they are called, data are called arguments
 can put things in parenthesis to enable function to pass data via new variables 
 if statement will allow a function to do different things depending on certain 
 conditions - see indetentations to understand contents of if statements

### EQUAL Signs

 EQUAL SIGNS
 Single equal sign is assignment operator
 double equal sign checks if two values are equal 

### Concatenation and F-Strings

 concatenate strings - means link strings together in a chain or series
 means you can combine strings with other strings or variables
 One Example of Combining strings and variables together

```
   # print("You chose" + player + "computer chose" + computer)
```

 quite often in programming there's multiple ways to do the same thing 
 another option is called f-strings 
 f-strings allows you to make strings with other variables and python code
