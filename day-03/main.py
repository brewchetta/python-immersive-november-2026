## Topics

# - Python class syntax
# - Instances vs classes
# - Class instance attributes
# - Building instance methods
# - Utilizing the self parameter
# - Class attributes
# - Building class methods

# CLASSES #######################################################################################################

# the class below is sort of like a blueprint for building robots --- each time I want a new robot I can use Robot class to effectively print a new one and all the robots will have shared characteristics

# CONVENTION: the class is generally going to be named with CamelCase

class Robot:
    
    # instance methods
    def do_math(self):
        return "BEEP BOOP DOING MATH"

    # self is the instance (the individual) that used the method (ex. wall_e or r2d2)
    def greet(self):
        print(f"I am {self.name}")
        return "BEEP BOOP GREETINGS"

    def automate(self):
        return "BEEP BOOP AUTOMATING TASKS"

    # self is ALWAYS the first argument
    def target_enemy(self, enemy):
        return f"BEEP BOOP TARGETING {enemy}"

    def aid_friend(self, friend):
        return f"BEEP BOOP HELPING {friend}"

    # __init__ is a special double underscore or "dunder" method which is only called when a Robot is first built
    def __init__(self, name, functionality):
        self.name = name
        self.functionality = functionality

    # representation
    def __repr__(self):
        return f"Robot(name={self.name}, functionality={self.functionality})"



wall_e = Robot("Wall-E","stack blocks")
# name is an attribute and we can set or see attributes at will

# using explicit keyword args is the convention when making new instances
r2d2 = Robot(name="R2D2", functionality="sass")

# r2d2 and wall_e are INSTANCES of the Robot class


class Animal:
    
    def __init__(self, species, animal_class):
        self.species = species
        self.animal_class = animal_class
        self.health = 10
        # health is hardcoded to start at 10, we don't have a parameter for it

    def __repr__(self):
        return f"Animal(species={self.species}, animal_class={self.animal_class})"

    def eat(self):
        self.health += 1

    def fight(self):
        self.health -= 1
        if self.health <= 0:
            return f"{self.species} went extinct"





class Schedule:
    pass