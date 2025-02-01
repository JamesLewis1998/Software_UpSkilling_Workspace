# Workspace Overview

Repository to contain all work conducted within Fleetcode and Python Training. Contents includes: 

1. LeetCode Programming Practice
2. Youtube Python for Beginners 
3. IIY Advanced Training Course in Python
4. _Sequencing in PlantUML for Adhoc Arch work_ 

## Key Learning Points from RPS Example

Quick Notes from initial introduction:

- = means assign operator 
- A string is a sequence of characters used to represent text

***The Importance of Brackets:***

They can denote a list, a dictionary, an array, or a tuple, and they're also used in function and method invocations. Misuse of brackets often leads to syntax errors and bugs.

### Indentation 

1. Indentation is important - any line of code indented same amount is considered to be in that function
2. Return indicates whats returned when function get_choices is called (for example)

**Greeting to Console Example**

```
  def greeting (): 
       return "hi"
   response = greeting ()
   print (response)
```
- def in python is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function
- In Python, a function is a logical unit of code containing a sequence of statements indented under a name given using the “def” keyword
- In python you do not need to put anything at the end of each line 
- print response returns to console

### Dictionaries 

A dictionary is a data structure that maps one value to another - kind of like how an English dictionary maps a word to its definition.

1. Dictionaries - in python they are used to store data values in key value pairs
2. Dictionaries denoted by "dict" 
3. Curly braces begining and end with key value pairs separated by comas
4. Curly braces indicates at code level is used to define a Dictionary

**Dictionary Example**

Example shown below to illustrate dict definition, key value pairs and mapping between key and value:

```
dict = {"name": "beau", "colour" : "blue"}
```
- Key is name and colour, value is beau and blue 
- value can be a variable eg could set to choices 
- surround by quotation marks its a string
- In example above can define dictionary name by typing name instead of dict and 
 adding curly brackets in - the curly brackets are the indicators of the dictionary definition in code, not the word "dict"

### Inputs 

Inputs are used to define inputs from the user to get inputs from them 
whatever the person enters in this field gets saved against the variable in programme

**Inputs Example**

Example below illustrates defining an input as "Enter A Number" and printing a return in the console as "You Entered:", the displaying the number

```
number = input("Enter a value: ")  
print("You entered:",number)  
```

### Python Libraries 

 1. Python libraries are a set of useful functions so you don't have to learn 
 how to write python from scratch
 2. With basic pyhton its hard to get a programme to do something randomly
 import statements used to import libraries and usually put at top of programme

### Lists

Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

- List in pyhton used to store multiple items in a single variable
- Brackets are important in programming to ilsturate what the parameters purporse is

**Lists Example**

```
food = ["pizza", "burger", "pasta"]
dinner =random.choice(food)
print (dinner)
```
### Functions

**Functions** in Python. You use functions in programming to bundle a set of instructions that you want to use repeatedly or that, because of their complexity, are better self-contained in a sub-program and called when needed. That means that a function is a piece of code written to carry out a specified task.

 1. Functions can recieve arguments when they are called, data are called arguments
 2. You can put things in parenthesis to enable function to pass data via new variables 
 3. "if" statement will allow a function to do different things depending on certain 
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

Note, quite often in programming there's multiple ways to do the same thing - another option is called f-strings. F-strings allows you to make strings with other variables and python code

### IF, Elseif, Elif Programming

- else and elif statements - else if is a combination of if and else statements 
-elif - looks at the if conditions then move onto elif to consider if statement within
 
```
 else statement 
    age = 20 
    if age >= 18: 
        print("adult")
    elif age > 12:
        print("teen")
    elif age > 1:
        print("child")
    else:
        print("baby") 
```
Note, can also check for two conditions at once 

### Refactoring 

 Refactoring is the process of resturcturing code whilst keeping original functionality 
 common to refactor code to make it simpler or more understandable @ a quick glance
 nested if statement makes code more understandable at a quick glance 

_Example_: can put an if inside another if elif or else statement

### Sequencing of a Programme

Note, once you return something, the rest of the code in a function does not run, so where something is place is sequential to this return statement, placement of indentations in programming matter - driving sequence of functions and order of which they are executed in 