"""
Dictionaries are used to store infrmation of different data types
"""
family = {
    "Aditya": "Coder",
    "Saksham": "Cricketer",
    "Money": "Brother",
    "Shubi": "Snapchat",
    "Anant": "Big Brother",
    "Abhinav": "Brother part 2"
}

print(family)

# printing value of individual elements
print(family["Aditya"])

# adding new item to the dict
family["Avi"] = "Younger brother"
print(family)

# the order in which the items are being added to the dict doesn't matter
# the keys are immutable, therefore lists cannot be the keys
# the tuples can be the key

# keys are unique
# the last value of the key is taken
# if different values are assigned to the same key, the last entered value is considered
family = {
    "Aditya": "Coder",
    "Saksham": "Cricketer",
    "Money": "Brother",
    "Shubi": "Snapchat",
    "Anant": "Big Brother",
    "Abhinav": "Brother part 2",
    "Aditya": "He is also a programmer"
}

print(family)



# delete items
del family["Aditya"]
print(family)

# clear the dict - delete all the items
# family.clear()
# print(family)

# get() and if the key doesnt exist

while True:
    dict_key = input("Enter Name: ")
    if dict_key == "quit":
        break
    if dict_key in family:
        description = family.get(dict_key, "We don't have a "+ dict_key) # .get(key) gets the value of the key
        print(description)
    # else:
    #    print('We dont have '+ dict_key)

# iterate over the keys
for keys in family:
    print(keys)

for keys in family:
    print("the values for "+ keys +" is "+ family[keys])


# the key is hashed, the order in which you put the keys, might not the order in which they are stored
# the hash is used to store passwords in the databases
# the keys are hashed and the hash values are used to know in what slots the values of the keys are kept

# every time the program runs, a new dictionary is created


# PRINTING THE DICT. 5 TIMES
print('*' * 50)
for i in range(6):
    for keys in family:
        print("the values for "+ keys +" is "+ family[keys])           
    print('*' * 50)


# create a list of the keys of the dict and then print the values, they will be in an order.
# Use this only when you need to process in order

# .keys(), .values(), .items()
print(family.keys()) # will print a dict_keys object
print(family.values()) # will print a dict_values object
print(family.items()) # will print a dict_items object, with name-values pair as tuples

print("---------- Way 1 ------------")
ordered_keys = list(family.keys())
ordered_keys.sort()
for key in ordered_keys:
    print(key)



print("---------- Way 2 ------------")
# BETTER WAY
ordered_keys2 = sorted(list(family.keys()))
for key in ordered_keys2:
    print(key)



print("---------- Way 3 ------------")
# BEST WAY
for key in sorted(list(family.keys())):
    print(key)


print("---------- Printing Values only ------------")
# Print only the values
for val in family.values():
    print(val)


# Python Automatically updates the keys
print("---------- Before Update ------------")
for key in family.keys():
    print(key)

family["Saransh"] = "Same Brother"


print("---------- After Update ------------")
for key in family.keys():
    print(key)


# dict_keys([]), dict_values([]), dict_items([]) are View Objects

# DICT TO TUPLES -> .items() and tuple()
print('Dict to Tuples')
print('Dictionary')
print(family)
print('----------')
print(family.items())
print('----------')
f_tuples = tuple(family.items()) # tuple is a function that extracts tuples from a list
print(f_tuples)
print('---All key-values in tuples-------')
for tup in f_tuples:
    print(tup)



# TUPLES TO DICT -> .dict()
print('Tuples to Dict')
print(dict(f_tuples))

print('---------------------------------------------')
# UNPACKING THE TUPLE
print('UNPACKING THE TUPLE')
for i in f_tuples:
    name, value = i
    print(name +' '+ value)