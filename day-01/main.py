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