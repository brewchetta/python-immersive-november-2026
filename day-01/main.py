# In order to use this file, open a new terminal and type
# python day-01/main.py
# OR
# python3 day-01/main.py

# THIS IS A COMMENT

# What do you know about Python?

# object oriented programming language
#   object oriented programmin / OOP: create coding objects which fall into categories and share behavior

# automation - makes things simpler by making them scheduled or automatic

# bots - chatbots, scrapers, AI

# python has simple syntax

# server - django, flask, fastapi

# #######################################################################

print( "Hello world" ) # print will put something on the screen and doesn't do anything else

print( "How are you today?" )

# REPL - Read Evaluate Print Loop
# python -i main.py

# VARIABLE
# a way to store data for later use

# name              value
i_am_a_variable = "I am indeed a variable"

# variables are changeable
i_am_a_variable = "blah blah blah"

# you shouldn't change a constant... but you can change
MY_CONSTANT = "I am a constant... sort of"
MY_CONSTANT = "I shouldn't be changed but I was"

# variable names are usually in snake case
# you also use camel case but only for classes
# class CamelCase

# you can break any of these rules... but pythonistas will be upset

# with a variable you are either: 
# - DECLARING it, 
# - you are ACCESSING it, 
# - or you are REDEFINING it


# STRINGS ####################################################################

my_string = "I am a string"

# strings are usually text, you can id them by the fact that they're in quotes

alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers_string = "1234567890"

special_characters = "!@$%&*^&((*)&)()"

single_quotes = 'I am a string too!'

# formatted string / f string
general_greeting = "Hello"
time_of_day = "morning"
formatted_string = f"{general_greeting}! It is now {time_of_day}"
# 'Hello! It is now morning'
# f strings only work with "" double quotes

# concatenation
"string one" + " " + "string two"
# "string one string two"

first_name = "Chett"
last_name = "Tiller" 
first_name + " " + last_name
# 'Chett Tiller'

# length
len( first_name ) # 5
len( last_name ) # 6
len( "   " ) # 3 - empty spaces are still characters and contribute to length!

# NUMBERS #########################################################################

ten = 10

# integers are whole numbers
1
5
-30

# floats are numbers with decimals
5.0
1.9
1.00009
-0.19

# you can use type() to figure out what type of data you're using
type( ten )         # <class 'int'>
type( "hello" )     # <class 'str'>


# READING ERROR MESSAGES ##############################################

# some types don't play well together...
try:
    "10" + 10 # this will error out because the types aren't the same!
except:
    print("I couldn't add \"10\" to 10") # this will happen instead of the error

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str


# BOOLEAN ###########################################################

lightswitch = True      # the light is on
lightswitch = False     # the light is off

# make sure you're using capital "T" True and not lower "t" true


# FUNCTIONS #########################################################

# a callable set of instructions which do something

# function definition
def make_sandwich():
    # everything in the indent is part of the fn code
    print("1. Gather ingredients")
    print("2. Lay out two slices of bread")
    print("3. Add sauce to bread")
    print("4. Add other ingredients to bread")
    print("5. Close bread together")
    print("6. Eat sandwich")

# if it's not in the indent we have left the fn

# call/trigger/activate/invoke the fn
make_sandwich()

# you can repeat a fn call as many times as you need which makes them powerful
make_sandwich()

# fns can take INPUT and generate OUTPUT

# INPUT
def greet_user(username, time):
    print( f"Hello {username}! It is currently {time}" )

# by using arguments (the special name for input) we can make fns MORE FLEXIBLE
# parameters are the placeholder variables before we call the fn with concrete args

greet_user("Chett", "12pm")

# you may use variables for your arguments
user_1 = "Chett Tiller"
current_time = "12am"
greet_user(user_1, current_time)

# you can use keyword arguments to change how the args get put in
greet_user( time=current_time, username=user_1 )
# this has the same output as the fn call above still!


# default argument
def with_default(name, age=21):
    return f"{name} is {age}"

with_default("Chett") # "Chett is 21"
# it uses the default because we didn't give it an age

with_default("Chett", 19) # "Chett is 19"
# the age we put in (19) overrides the default age

def authenticate(username, password, role="user"):
    pass # fns need something in them and `pass` stands for "something will go here later"


# OUTPUT

def addition(num_1, num_2):
    return num_1 + num_2


def return_early():
    return "I am the return"
    print("I come after the return")

def multiple_returns():
    return 1 # only the first evaluated return happens ALL THE REST GET IGNORED
    return 2
    return 3
    return 4



# IMPORTANT: each fn should only have one responsibility!

def system_check():
    print("All systems are go!")

# this fn uses other fns and calls them in the order that we need to
def bootup():
    greet_user(user_1, current_time)
    system_check()


# you can create fns in fns
def outer_fn():

    def inner_fn():
        print("I am the inner fn")

    inner_fn()

outer_fn()

# you can pass fns as arguments to other fns
def call_three_times( callback_fn ):
    callback_fn()
    callback_fn()
    callback_fn()


# SCOPE

# this is the global scope and everything here is available in all other scopes
the_world = "I am the world"
times_run = 0

# everything tabbed in for the fn is inside of the fn
def what_is_the_world():
    global times_run
    # pulls times_run from the global scope
    # local scope
    print( the_world )
    # increment by one
    times_run += 1
    print(f"Times run: {times_run}")
    the_last_thing = "I am the last thing"
    # return the_last_thing <<< this is the only real way to get a local variable out of a fn


# CONDITIONALS ############################################################################

# if this:
#     whatever
# else:
#     do something else

# Comparison Operators

10 > 9 # True

len("hello") >= 5 # True

current_count = 0

# two equals means we are checking the value NOT setting it
current_count == 10 # False

current_count = 10

current_count == 10 # True

# you can also check that something is NOT equal
current_count != 10 # False

# you can make sure two (or more) conditions are true with an `and`
current_count > 9 and type( current_count ) == int # True
current_count > 9 and type( current_count ) == float # False

# you can see if either of two (or more) conditions are true with an `or`
current_count > 9 or current_count < -9 # True

def double_digits(number):
    if ((number > 9 and number < 100) or (number < -9 and number > -100)):
        return "Double digits"
    else:
        return "Not double digits"

# you don't need to have an `else` with every `if`
def just_if(password):
    if (password == "password123"):
        return "Password accepted"

# from datetime import datetime

# current_time = None

# current_time = datetime.now()

current_time = 14

# elif allows us to check multiple conditions in sequence
# if the previous condition is False it moves on to the next one
# however if a condition is True, it ignores all the later conditions
def get_time_based_greeting(current_time):
    if (current_time < 12):
        return "Good morning"
    elif (current_time < 18):
        return "Good afternoon"
    elif (current_time < 22):
        return "Good evening"
    else:
        return "Good night"


# TRUTHY / FALSEY VALUES

# every value in Python has an inherent truthiness or falsiness to it

# falsey values tend to be non-existent or empty values

# you can test truthy or falsey with the `bool()` constructor which turns it into True or False

bool( 1 ) # True
bool( 0 ) # False
bool( -1 ) # True

bool( "Hello" ) # True
bool( "" ) # False
bool( "     " ) # True

bool( None ) # False

bool( ["I am a list"] ) # True (the list has something inside of it)
bool( [] ) # False (the list is empty)

def is_not_zero(number):
    # we can use truthiness to check if something is not zero
    if (number):
        return "It's not zero"

def authorize(password):
    # we can use truthiness to check if a string has length (if it exists basically)
    if (password):
        if (password == "password123"):
            return "Correct password"
        else:
            return "Incorrect password"
    else:
        return "Please type in a password, you did not type anything in"


# EXERCISES ##################################################################################

# 1. Build the function `say_my_name()` which accepts a `first_name` and a `last_name`
#   The function returns the name as a single full name
#   Example: say_my_name("Chett", "Tiller") --> "Chett Tiller"

def say_my_name(first_name, last_name):
    pass

# 2. Build the function `is_a_string()` which accepts a single argument `arg`
#   The function returns either "STRING" if `arg` is of type `str` or else "NOT STRING"
# Example: is_a_string("hello") --> "STRING"
# Example: is_a_string(07734) --> "NOT STRING"

def is_a_string(arg):
    pass

# 3. Build the function `stoplight()` which accepts a single argument `color`
#   The function returns "GO" if `color` is "green", "SLOW" for "yellow" and "STOP" for "red"
#   If `color` is none of those three, return "OH NO"
# Example: stoplight("green") --> "GO"
# Example: stoplight("red") --> "STOP"
# Example: stoplight("aquamarine") --> "OH NO"

def stoplight(color):
    pass

# 4. Build the function `fizz_buzz()` which accepts a single argument `number`
#   The function returns "fizz" if `number` is divisible by 3, "buzz" if divisible by 5
#   Return "fizzbuzz" if divisible by both and just the number if divisible by neither
# Example: fizz_buzz(6) --> "fizz"
# Example: fizz_buzz(10) --> "buzz"
# Example: fizz_buzz(30) --> "fizzbuzz"
# Example: fizz_buzz(31) --> 31

def fizz_buzz(number):
    pass

# 5. Build the function `average()` which accepts two arguments `num1` and `num2`
#   The function return the average of the two numbers
#   Average is calculated as the sum divided by the total number of numbers
# Example: average(10, 20) --> 15
# Example: average(-10, 10) --> 0

def average(num1, num2):
    pass