# ========== Classes ==========

print( "Classes")

## ======= Classes =========
    # Classes in python can be declared in python
    # from the classes we can instantiate an object
    # An object is an instance of a class 
    # A class is a type of an object

# Example: Creating a Class called Dog
class Dog: 
        def bark(self):                 # Now define a method for the class
                                        # Self as an arguement of the method will point to the current object instance
                                        # And must be specified when defining a method inside a class
                                        # So when you're creating a method inside a class you're always going to start with self
            print("woof!")

roger = Dog()
print(type(roger))                      # Returns <class '__main__.Dog'> in command line
                                        # Meaning roger is a Dog class, ie roger is a Dog

# Init is a special type of method which is a constructor
    # We can use constructors like the one below to initialise one or more properties when we create a new object from that class

class Cat:
    def __init__(self,name,age):        # We always have to add self, but on top of this have added name and age
            self.name = name            # Name and age are two variables we can pass in when we create a dog
            self.age = age              # the two variables will then be associated with that object

    def meow(self):                     # This is the method for the class
          print("meow")                 # Meow is the output of the method and self is the arguement for the method 


lucas =Cat("lucas",5)                   # Now when we run the programme it will create a cat and assign the name to self.name and self.age
print(lucas.name)                       # lucas.name == self.name above which is how you access the constructor info inside the function
print(lucas.age)                        # lucas.age == self.age above 

lucas.meow()                            # When you run this in the programme the programme lucas == self 
                                        # The output in the command window will be printing meow as lucas has been defined as a cat and
                                        # One of the methods of the class is the Meow method which prints meow in the cmd window

## ======= Inheritance in Classes =========
    # Example of inheritance as follows - create a new class before the dog class

class Animal:
      def walk(self): 
            print("walking")            # Class defined with walk method defined

class Dog (Animal):                     # By putting Animal in brackets, the dog class is going to inherit from the Animal Class
    def __init__(self,name,age):        # As before innit used to define self with assignment of name and age
            self.name = name 
            self.age = age 
    
    def bark(Self):                     # Class defined with bark method defined
          print("woof!")                # Prints woof when run
        
roger = Dog("Roger",8)                  # roger defined as Dog class with Name and Age in Brackets 

print(roger.name)
print(roger.age)

roger.walk()                            # Notice how dog class does not actually have a walk method but is getting this from the animal class
                                        # Ie. it is inheriting the walk method from the Animal class
                                        # This way you could create 10 different classes for animals, all of which could inherit the same class 
                                        # for walking, avoiding repitition in programming by all the inheritance to happen via the brackets (Animal )
roger.bark()