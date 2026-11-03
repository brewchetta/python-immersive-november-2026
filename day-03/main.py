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

    # class variable
    all_tasks = []
    color = "blue"
    completed = False

    def __init__(self, day_of_week, time, task):
        self.day_of_week = day_of_week
        self.time = time
        self.task = task
        Schedule.all_tasks.append( self )

    def __repr__(self):
        return f"Schedule(day_of_week={self.day_of_week}, time={self.time}, task={self.task}, completed={self.completed})"

    def complete_task(self):
        self.completed = True

    # a class method is attached to the class (Schedule) instead of an instance
    @classmethod
    def tasks_by_day(cls, day):
        return [task for task in cls.all_tasks if task.day_of_week == day]

    # we call class methods like so:
    # Schedule.tasks_by_day("Tuesday")

    @classmethod
    def clear(cls):
        cls.all_tasks.clear()

    @classmethod
    def add_task_everyday(cls, task, time):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for d in days:
            Schedule(task=task, time=time, day_of_week=d)

soccer = Schedule("Tuesday", "6pm", task="soccer practice")
Schedule("Monday", "3pm", "karate")
Schedule("Tuesday", "9pm", "movie night")
Schedule("Thursday", "12pm", "lunch with Bob")


# INHERITANCE ####################################

# superclass
# subclasses can inherit the behavior of the superclass

class Cat:

    claws = True

    def __init__(self, name, number_of_lives):
        self.name = name
        self.number_of_lives = number_of_lives

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, number_of_lives={self.number_of_lives})"
        # .__class__.__name__ gets the class name of the current instance instead of just the superclass name

    def scratch(self):
        return "Scritch scratch there goes all your nice furniture"

    def use_night_vision(self):
        return "This cat can see in the dark!"


# mixins are just superclasses with a smaller subset of methods or behaviors
class RoarMixin:
    def roar(self):
        return "rawr"

# a subclass can inherit from multiple classes!


# D.R.Y. - dont repeat yourself

# Tiger inherits from Cat superclass
class Tiger(Cat, RoarMixin):
    
    # defining a method in the subclass that has the same name as a superclass method means the subclass method gets priority
    def scratch(self):
        return "NOT JUST A SCRATCH --- WATCH OUT!"

    def swim(self):
        return "it's not doggy paddle it's tiger paddle"


class Lion(Cat, RoarMixin):
    
    def __init__(self, name, number_of_lives, mane_size):
        # run the Cat __init__
        super().__init__(name, number_of_lives)
        # and then add mane_size
        self.mane_size = mane_size

    def __repr__(self):
        # use the super class repr and then add mane size to the end of the string
        return super().__repr__()[:-1] + f", mane_size={self.mane_size})"
        # [:-1] removes the trailing parentheses

    def use_night_vision(self):
        print("I see in the dark")
        return super().use_night_vision()




tony = Tiger(name="Tony", number_of_lives=10)
mittens = Cat(name="Mittens", number_of_lives=9)

cowardly = Lion(
    name="Cowardly Lion", 
    number_of_lives=1, 
    mane_size="shoulder to mid back"
)