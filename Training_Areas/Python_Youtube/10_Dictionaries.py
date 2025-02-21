# ========== DICTIONARIES IN PYTHON ==========

print( "Insert Section Title here")

## ======= Creation and Modify of Dictionary =========
# Lists allow you to create collections of values, dictionaries allow you to create key value pairs
# For example:

dog = {"name":"roger"} # Remember can use either "" or '' for strings
                       # Common to spaces between things so it's easier to read
                       # Key can be any immutable value - i.e. unable to be changed
                       # key can be string, a number a tuple 
                       # value can be anything you want
dog = {"name":"roger","age":10,"colour":"blue"}
print(dog["name"])     # Prints roger in terminal

# Changing values stored at a specific index: 
dog["name"] = "ben"    # Replaces roger with ben
print(dog) 

# Another way to get a specific element is to use the Get Method
print(dog.get("age"))

# Useful mechanism to set up default values via the above mechanism 
dog.get("colour","brown")         # This way if there's no colour found or value for colour - the default allocated is brown
print(dog.get("colour","brown"))  # The get method allows you to assign a default colour

## ======= Deleting Entries in Dictionary =========
# Can use the pop method to delete entries in the dictionary as follows
dog.pop("name")
print(dog) # will return {'age' : 10    } because the key and associated value has been deleted

# Can also use pop item method - retrieves and removes last key value pair entered into the dictionary 
# Retrieve and remove the last key value pair inserted into the dictionary 
print(dog.popitem())    # During colour example {"colour" :"blue"} was added into the dictionary 
print(dog)              # Dog now returns {"age" : 10} because popitem removes the last item added into the dictionary


## ======= Check if a key is Contained in a Dictionary =========
# Examples:
print("name" in dog) # returns false 
print("colour" in dog) # returns false
print("age" in dog) # returns true 

print(dog.keys()) # will show/ return ['age']
print(dog.values()) # will show/ return ['10']

print(list(dog.items())) # to put each item of the dictionary in a list 
                         # the above returns [('age','10')]
                         # Note if dog = {"name":"roger","age":10,"colour":"blue"}
                         # the command would return [("name","roger"),("age",10),("colour","blue")]

# Also can assess length of dictionary same way you would with tuples and lists
print(len(dog)) # Returns 1 because the only key in there is "age"

## ====== Adding Key Value Pair to Dictionary =====
# Example below:
dog["name"] = "roger" # Adding of the key and associated value of roger back into dictionary
print(dog)
del dog["name"] # removes/ deletes key and associated value of name in dictionary
print(dog)

# ===== Copying Dictionaries =====

dogcopy = dog.copy() # dogcopy becomes the new/ copied version of the dictionary
print(dog)
print(dogcopy)
