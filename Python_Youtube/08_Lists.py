# ========== Lists ==========

print( "Lists")

## ======= Creation and Functions =========
# These are an essential python data strcuture 
# allows you to group together multiple values and reference them with a common name 
# Can have different types of data types in a single list too

from enum import Enum
class Gender(Enum):
    MAN = 0
    WOMAN = 1
    UNDEFINED = 2

FamilyTree = ["Derek",26,Gender.MAN,"Roger",44, Gender.MAN,"Lily",7,Gender.WOMAN]

# Can check whether an item is in a list by using the in Function
print("Dean" in FamilyTree) #returns false 
# If Dean is in FamilyTree, you're printing the outcome of the statement 

# Index's in lists - remember in programming we start at 0
print(FamilyTree[2]) # returns Gender.MAN

#Can also replace a value through indexing prior to printing result
FamilyTree[1] = 26
print(FamilyTree) # Now replaced 26 with 27 as a result of the new index

# Using what we've learnt before about indexing can use negative to start at other end
print(FamilyTree[-3]) # this will return "Sophie"

## ======= Extracting parts of a list =========
# Use colon to extract a slice of the list for example
print(FamilyTree[4:8])
# returns the values [24, <Gender.MAN: 0>, 'Sophie', 18]
# value 4 is 24
# value 5 is Gender.MAN
# Value 6 is "Sophie"
# value 7 is 18 

# Note, if you leave the start or the end of the [] as blank it will either 
# start at the beginning of the list or run to to the end of the list

## ======= Extend and Append Methods =========
# Append is a way to add something onto the end of the list 
FamilyTree.append("Susan") # Note append only accepts one argument, so including more than one input in the
                          # brackets will return an error 
print(FamilyTree)

# Another way to achieve this and actually add multiple values in at once is appending two lists together via
FamilyTree.extend([58,Gender.WOMAN,"Richard", 63,Gender.MAN])
print(FamilyTree)

# Can also use the plus equals operator to do the same thing as extend
# The mechanism here takes the list and adds the additional items to the end 

FamilyTree += ["Gerald", 10,Gender.MAN] # Don't forget square brackets or it puts each letter individually in the list
                                      # this only applies if the only thing we were adding was "Gerald"
print(FamilyTree)

## ====== Removing Parts of a List =====
# Using. remove For example:
FamilyTree.remove("Richard")
FamilyTree.remove("Gerald")
print(FamilyTree)

# Using .pop for Example: 
print("Using Pop for Example")
print(FamilyTree.pop()) # returns <Gender.MAN: 0>
# pop removes the last item of the list and returns it 
print(FamilyTree)

## ===== Adding Items to Specific Points in a List =====

#Start off with a new list for this example: 
items = ["apple","orange","pear","banana","grapes"]
print(items)
# Apple is 0, orange is 1, pear is 2 - character referencing
items.insert(2,"peach")
print(items)
# to add multiple items at a specific index need to use slice
items[1:1] = ["grapefruit","pineapple"]
print(items)
# Here we add in at character 1 -> [1:1] means between characters 1 and 1 
# introduced multiple items into the list starting and end at index 1

## ====== Replacing Multiple items in a list =======

items [2:5] = ["kiwi","coconut"]
print(items) # this actually replaces characters 'orange' and 'peach indexed at 3 and 4 with 
#"kiwi" and "coconut"

# ===== Sorting Lists ===== 
items = ["apple","orange","pear","banana","grapes"]
# Note sorting is not supported in a list containing ints and strings 
print(items)
items.sort() # integers or floats are sorted into numerical order
                    # strings are sorted into alphabetical orders 
print(items)  

# Note sort orders upper case letters first followed by lowercase ones 
items = ["apple","orange","pear","Banana","Grapes"]
items.sort()
print(items)
# To remedy this use within sort the following: 
items.sort(key=str.lower)    # Now sorts without caring about upper or lower case in list
print(items) 

# ====== Avoiding Modofiying original list ======

itemscopy = items[:] #slice with nothing at the beginning or the end - therefore copies whole list
print(itemscopy) # the way in which these are used sequentially is important to ensure not overwriting the original list 

items = ["apple","orange","pear","Banana","Grapes"]
# Also ways to sort a list without modifying the original list 
# Global Function called sorted 
print(sorted(items,key = str.lower))
print(items) # Will see from doing this we're still printing the original list because the function above being printed 
# does not override the original items list function