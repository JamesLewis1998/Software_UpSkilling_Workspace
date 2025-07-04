# ========== Variable Scope ==========

print( "Variable Scope")

## ======= Declaring Variables =========
    # When you declare a variable that variable is visible in parts of your programme depending on where you declare it
    # If you declare a variable outside of a function, the variable is visible to any code running after the declaration including functions
        # This kind of variable is known as a global variable 

# For Example: 
age = 8             # age is now a global variable as its declared outside of all functions 
def test():         
    print(age)      # print(age is the body of this function and the function test() output 

print(age)          # output in the command terminal is 8 because age is a global variable 
test()              # Running test prints the age in the command window because internal to the function there is a command to print age in the functions body 

# A function declared inside the function becomes a local variable
def test1():
    age1 = 10
    print(age1)

# print(age1) will return an error in the command window/ terminal because age1 is defined inside the function test1 and not declared globally
print(test1())      # Will return an output of 10 in the command terminal because the body of test1 has age1 declared internally to the function

## ======= Nested Functions =========
    # Functions in python can be nested inside other function
    # A Function inside another Function is visible only inside that function 
    # Useful to create utilities that are useful to a function but not useful outside of it 

    # Why hide a function if it does not harm? 
        # Always best to hide functionality that is not useful elsewhere
        # Also enables us to make use of closures

# For Example: 

def talk(phrase):               # Function Talk
    def say(word):              # Inside the Function Talk we have say - input into say function is word 
        print (word)
                                # We can call the say function inside the word function
    words = phrase.split(' ')   # Split is a way to create a list out of a string -> Split's on every space hence (' ')
    for word in words:          # For every word in the words list
        say(word)               # We will run the say function with word -> ie we're going to print the word

talk('Iam going to buy the milk') 
                                # Function talk is ran, internal to the function, another function say is ran which prints words 
                                # Inside the function words is phrase split into a list where each word is a list item and the split is done on the space between the words as indicated by (' ')
                                # for word in word then runs as a loop and for every word in the words list we say the word, i.e. print the word 
# Result of above is the input into talk broken down into line by line elements in the command window 

## ======= Accessing Variables in different layers of a function =========
    # Accessing a Variable defined in the outer function within the inner function =========

def count():            # Function is called Count 
    count = 0               # Variable count defined as 0
    def increment():            # Inner Function called Increment Defined
        nonlocal count          # Allows us to access the count outside the Increment function
                                # If we do not call this nonlocal, we cannot access this variable from inside the increment function
        count = count + 1       # Define count as the count outside the function plus 1
        print(count)            # Final command of the inner function is to print the varaible count 
    increment()             # Count function command to run inner increment function 
count()                 # Now run count function in the python programme
                        # Count function outputs 1 in the command window because 0+1 =1

## ===== Closures and Use with Functions =====
    # If you return a nested function from a function that nested function has access to the varaibles defined in that function even if that function is not active anymore

# For Example: 
def counter(): 
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count            # Returning count from the nested function increment
    return increment        # From the outer function (counter) we're returning the nested function increment
increment = counter()   # Assigning outer (counter) function to variable increment 
                        # Note by calling increment, we're basically calling the returned inner function

# Now we're going to print the increment which is the counter as an output
# Note, because we're calling the inner function it's not going to reset the count to 0 everytime and can keep track of that value
    #
    # Therefore when running the function for the first time the return is 1
    # The second time the return will be 2
    # The third the return will be 3
# Return the increment inner function which still has access to the state of the count variable even though the counter function has ended
 
print(increment())          # Returns 1
print(increment())          # Returns 2
print(increment())          # Returns 3