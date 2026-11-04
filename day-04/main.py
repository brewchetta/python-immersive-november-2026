# LAMBDA #################################################################################################

# in js a lambda is similar to an arrow fn

def say_hello(name):
    return f"Hello {name}"

# name      lambda  arg     body / return
say_hello = lambda name: f"Hello {name}"

# lambdas have an implicit return meaning they return automatically

# lambdas are meant for short, one line functions

def do_3_times( other_fn ):
    other_fn(1)
    other_fn(1)
    other_fn(1)

do_3_times( lambda x: print(x + 1) )

# a lambda with no arguments
say_goodbye = lambda: "Goodbye"

# a lambda with lots of arguments
add_together = lambda x,y,z: x + y + z


# ARGS & KEYWORD ARGS #######################################################################################################

def some_fn(thing, item, other_thing):
    return f"{thing} {item} {other_thing}"

# keyword arguments
some_fn(other_thing=3,thing=1,item=2)

def super_addition(*args):
    return sum( args )

# *args allows to accept ANY number of argument
# args in the fn will be a tuple

# kargs stands for keyword arguments
def accepts_keywords(**kargs):
    print( kargs )

# kargs comes through as a dictionary

def send_request(**kargs):
    kargs["headers"]
    kargs["authorization"]
    kargs["cookies"]


def super_math(operator, initial_value, *args, **kargs):
    result = initial_value

    if operator == "+":
        result += sum(args)

    elif operator == "-":
        result -= sum(args)

    # if someone put in the keyword absolute=True
    if kargs.get("absolute"):
        result = abs(result)

    # if someone put in the keyword round=True
    if kargs.get("round"):
        result = round(result)
    
    return 
    
# args and kargs are conventions, you may instead do *stuff, **

import random

def guess_the_number(*args):
    random_number = random.randint(0,100)

    for num in args:
        if num == random_number:
            return f"Congratulations you guess {random_number}!"

    return f"You did not guess {random_number}..."


def describe_person(**kargs):
    description = "This person is..."

    for key in kargs:
        description += f" {key} is {kargs[key]}"

    return description



class Person:

    # kargs allow us to take in any number of attributes for instance
    def __init__(self,**kargs):
        for key in kargs:
            setattr(self, key, kargs[key])
            # setattr is a special way of setting an attribute

    # THIS IS DANGEROUS - people can abuse this system to overwrite some of the really important functionality of your instance so be careful with it...

chett = Person(name="Chett", age=21, address="Somewhere")


# IMPORTS AND MODULES ################################

import random

# random is a module
# a module is additional pre-built code that we're adding to our file

random.choice([1,2,3,4,5])
# a random item in the list

# we can also import the choice fn from the random module
from random import choice

choice([1,2,3,4,5])

# you can also rename the import as you're importing it
from random import choice as random_choice
random_choice([1,2,3,4,5])


# for installing external packages in the terminal: pip install package_name

# to use it: import package_name

import requests

def get_dad_joke():
    # we need the headers for this API
    headers = {"Accept": "application/json"}

    # make a GET request to icanhazdadjoke.com
    response = requests.get("https://icanhazdadjoke.com", headers=headers)

    # if the response is a 200...
    if response.status_code == 200:
        # parse the json response and return the joke inside
        return response.json()['joke']
    else:
        # otherwise alert the user to the bad status code
        return f"[{response.status_code}] Unable to tell that joke..."