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