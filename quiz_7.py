# Quiz 7
# ======

# Q1: Which line of code will change the starting_dictionary to the final_dictionary?

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }

# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# final_dictionary = {}

# A
# final_dictionary = starting_dictionary.append({"c": 7})
# Worng. You cannot append to a dictionary

# B
# final_dictionary = starting_dictionary += {"c": 7}
# Obviously wrong with = and +=

# C
# final_dictionary = starting_dictionary["c"]: 7
# Obviously wrong with ["c"]: 7 hanging

# D
# final_dictionary = starting_dictionary["c"] = 7
# Obviously wrong with two = 

# E
# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary
# Correct

# print(final_dictionary)


# Q2: Which line of code will produce an error?

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# A
# dict["c"] = [1,2,3]
# OK. Reassigns "c"

# B
# for key in dict:
#     dict[key] += 1
# OK. Increment all values

# C
# dict[1] = 4
# OK. Creates a new key:value pair 1:4

# D
# print(dict[1])
# Error. There is no key 1 in dict

# print(dict)


# Q3: Which line of code will print "Steak"?

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# A
# print(order["main"][2])
# Wrong. This will print ['Steak']

# B
# print(order["dessert" - 1][2][0])
# Wrong. You cannot access dictionary items by location (e.g. key-1), only by key

# C
# print(order[main][2][0])
# Wong. There is no variable called main

# D
# print(order["main"][2][0])
# Correct. 
    # [2] accesses the value with key 2, 
    # [0] gets the first item from the list.
