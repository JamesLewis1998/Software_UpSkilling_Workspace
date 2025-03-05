# ========== Polymorphism ==========

print( "Polymorphism")

## ======= Overview =========
    # Polymorphism generlises a functionality so it can work on different types
    # Important concept in object orientated programming

# For Example, below we have defined the same method on different classes: 
    # Both the Dog and the Cat have eat methods

class Dog:
    def eat(Self):
        print('Eating Dog Food')
    
class Cat: 
    def eat(Self):
        print('Eating Cat Food')

# We can then generate objects and call the eat method regardless of the class 
# the objects belongs to and will get different results
    # Allocate which class which animal belongs to
        # ie animal1 belongs to Dog Class
        # animal2 belongs to the Cat Class

animal1 = Dog()
animal2 = Cat()

# Call the eat method regardless of the class the object belongs to
    # Call the eat method on both objects:

animal1.eat()    # Returns Eating Dog Food in the command terminal
animal2.eat()    # Returns Eating Cat Food in the command terminal

# This expands a lot for the generic capability. For Example:
    # Maybe you have a list of different animals and you could loop through that list and call the eat function or eat method on each 
    # method in that list and they don't have to be the exact same class to be able to run the eat method 

# So we've built a generlaised interface and do not need to know whether the animal is a cat or a dog
    # Just that we can call eat on it. 

# NOTE: 
    # In Python, self is a fundamental concept when working with object-oriented programming (OOP). 
    # It represents the instance of the class being used.
    # Whenever we create an object from a class, self refers to the current object instance