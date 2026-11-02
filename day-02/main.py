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

# two dimensional matrix - list of lists

simple_matrix = [
    ["X","O","X"],
    ["X","X","O"],
    ["O","X","O"]
]


# LOOPS ################################################################################

# why use loops?
# we often want to go through each item in a list and do something with it


# while loops

def print_all_items():
    my_list = [10,20,30,40,50]
    new_list = []

    # this index var is the currently selected index
    index = 0

    # while the index doesn't go past the end of the list....
    while index < len( my_list ):
        # do stuff over and over again
        current_item = my_list[ index ]
        new_list.append(current_item * 3)
        index += 1

    return new_list

# index = 0; print 10
# index += 1
# index = 1; print 20
# index += 1
# index = 2; print 30
# index += 1
# ...
# index = 5; end loop because index is not less than list length

my_list = [9,8,7,6,5,4]

# num is the stand in variable name for each item
for num in my_list:
    print( num )


counter = 0

# you can use _ if you don't care about the name for each item
for _ in my_list:
    counter += 1


def find_the_geese():
    birds = ["duck","duck","goose","duck","duck","goose","duck","duck"]

    num_geese = 0

    for current_bird in birds:
        if current_bird == "goose":
            num_geese += 1

    return num_geese


def ring_up():
    prices = [10.99, 12, 13.68, 14.40]

    subtotal = 0

    for price in prices:
        subtotal += price

    # subtotal = sum(prices)

    subtotal *= 1.0875
    return round(subtotal, 2)


# the sum divided by the total number of items
def get_the_average( list_of_numbers ):

    # in case of an empty list....
    if len( list_of_numbers ) < 1:
        return None

    # sum(list_of_numbers)
    total = 0

    for index in list_of_numbers:
        total += index

    return total / len( list_of_numbers )


# List Comprehension

def multiply_by_three( some_list ):
    # return a new list where each item is multiplied by 3
    return [ num * 3 for num in some_list ]

def even_or_odd( list_of_numbers ):
    return [ ("even" if num % 2 == 0 else "odd") for num in list_of_numbers ]

def evens( list_of_numbers ):
    # return the unchanged num if even
    return [ num for num in list_of_numbers if num % 2 == 0 ]

# List Comprehension Exercises

# return a new list using list comprehension to filter and only include words that contain 'g'
def words_with_g( list_of_words ):
    return [ word for word in list_of_words if 'g' in word.lower() ]

# return a new list using list comprehension of all prices rounded to the second decimal place
# [20.9999999, 15.3789, 22.8765] ---> [20.99, 15.38, 22.88]
def round_prices( list_of_prices ):
    price_list = [ round(n, 2) for n in list_of_prices ]
    return price_list


# SETS & TUPLE #########################################################################

# a set does not allow for duplicate data

my_set = { 1, 2, 3, 4, 4, 4, 4 }
# { 1, 2, 3, 4 }

# a tuple is like a list except it cannot be changed after you declare it
# (you can't add or remove items or change them)

my_tuple = (1,2,3,4,5)

my_tuple[0] # 1

# there is no append or pop
# cannot do: my_tuple[0] = 20