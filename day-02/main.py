## Topics

# - Python input function
# - Python dictionaries as a data structure
# - Python lists as a data structure
# - Python while loops
# - Python for loops

# Review ########################################################################

# VARIABLES
# declare information - changeable value

count = 0

# DATA TYPES

count = "Dracula"   # string - text
count = 10          # integer - whole numbers
count = 10.1        # float - decimal point numbers
count = True        # boolean - True or False

# FUNCTIONS
# a set of instructions - we can run that set of instructions whenever we call the fn

def increment_count():
    # pull count into this scope
    global count
    # local scope
    count += 1
    local_variable = "I am local"

# functions create a new local scope

# print(local_variable)

# functions allow for input and output

# parameters are placeholders for a fn's input
def addition(num1, num2):
    return num1 + num2
    # return is the output of a fn

thirty = addition(10,20)

# CONDITIONAL LOGIC

# if/else/elif

def what_is_the_count():
    # using the `elif`
    if count > 9:
        return "It's multiple digits"
    elif count < -9:
        return "It's multiple digits"
    else:
        return "It's one digit"

def what_is_the_count():
    # using the `or`
    if count > 9 or count < -9:
        return "It's multiple digits"
    else:
        return "It's one digit"


# INPUT FUNCTION
# input function pauses python execution to get type user input

def get_favorite_candy():
    prompt = "What is your favorite halloween candy? >>> "
    fav_candy = input( prompt )

    # it's up to you to validate the data
    if len( fav_candy ) == 0:
        print("You didn't type anything, we need your favorite candy")


# DICTIONARIES
# js objects

# data structures - a set format for dealing with values and sometimes keys
# these are pieces of data that are meant to hold more data

# dictionaries keys and values

        #    key    value    key  value  key      value
person = { "name": "Chett", "age": 21, "height": "6'2\"" }

person = {
    "name": "Chett",
    "age": 21,
    "height": "6'2\""
}

# python dictionaries expect keys to be strings

# reading from keys:
person["name"]  # "Chett"
person["age"]   # 21

# you cannot easily get a data that exists:
# person["address"] # this will cause an error

# we can avoid null value errors with .get()
person.get("name") # Chett
person.get("age") # 21
person.get("address") # None

# changing dictionary values
person["age"] = 19
person["name"] = "Chett Tiller"
person["name"] = "ChettGPT"

person["address"] = "123 Sesame St."

# nested dictionaries

def increment_reps():
    country["capital"]["capitol"]["representatives"] += 1

country = {
    "name": "US of A",
    "capital": {
        "name": "Washington D.C.",
        "population": 693645,
        "capitol": {
            "name": "The Capitol Building",
            "representatives": 435,
            "senators": 100,
            "increment_reps": increment_reps
        }
    }
}

# accessing nested data
country["capital"]["population"] # 693645
country["capital"]["capitol"]["representatives"] # 435

# you can still set information using nesting in this way
country["capital"]["capitol"]["representatives"] = 436

# you can still add new key / value pairs as well
country["capital"]["capitol"]["color"] = "light grey"