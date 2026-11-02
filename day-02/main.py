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


# INPUT FUNCTION ##############################################################
# input function pauses python execution to get type user input

def get_favorite_candy():
    prompt = "What is your favorite halloween candy? >>> "
    fav_candy = input( prompt )

    # it's up to you to validate the data
    if len( fav_candy ) == 0:
        print("You didn't type anything, we need your favorite candy")


# DICTIONARIES ###############################################################
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


# LISTS ##########################################################################

# data structure - hold data

# keys are less relevant - order

sandwich_instructions = [
    "First you get the bread",                  # index 0
    "Toast the bread I guess",                  # index 1
    "Put stuff in the bread",                   # index 2
    "Count the calories",                       # index 3
    "Eat the bread and the stuff in the bread"  # index 4
]

# index - the value's place in the list

sandwich_instructions[0] # "First you get the bread"
sandwich_instructions[2] # "Put stuff in the bread"
sandwich_instructions[4] # "Eat the bread and the stuff in the bread"
# sandwich_instructions[15] # this will give an error bc it goes past the end of the list

# counting from the back of a list
sandwich_instructions[-1] # "Eat the bread and the stuff in the bread"

# set items in the list using an index
sandwich_instructions[0] = "Think about sandwiches"

# list methods - a function attached to a list which manipulates it

sandwich_instructions.append("Clean up") # adds to the end of the list

sandwich_instructions.pop() # by default removes from the end of the list

sandwich_instructions.pop(0) # removes from the list at that index

sandwich_instructions.reverse() # reverses the list

sandwich_instructions.insert(0, "Buy bread") # adds a new item at index 0 (the front of the list)

# destructive vs non-destructive
# destructive means we directly change the original list
# non-destructive means we don't change the original list

sandwich_instructions[0:2] # gets items with indexes 0 & 1
sandwich_instructions[1:3] # gets items with indexes 1 & 2
sandwich_instructions[:3] # gets items up to but not including index 3
sandwich_instructions[2:] # gets items starting with index 2 and later

# nested lists

drinks = [
    {
        "name": "Water",
        "alcohol_content": 0,
        "ingredients": [ "hydrogen", "oxygen", "trace minerals", "fluoride" ]
    },
    {
        "name": "Bourbon On The Rocks",
        "alcohol_content": 40,
        "ingredients": [ "Noble Oak Bourbon", "rocks" ]
    },
    {
        "name": "Apple Juice",
        "alcohol_content": 0,
        "ingredients": [ "apples", "sugar", "citric acid" ]
    }
]

# a list nested in a dictionary nested in a list

drinks[0]["ingredients"][0] # "hydrogen"

# matrix

# two dimensional matrix - list of lists

simple_matrix = [
    ["X","O","X"],
    ["X","X","O"],
    ["O","X","O"]
]