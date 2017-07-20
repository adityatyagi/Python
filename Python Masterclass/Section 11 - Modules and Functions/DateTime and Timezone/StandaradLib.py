import random
import shelve

print(dir())
# anything that starts witha __ here, we shouldn't be changing
# https://docs.python.org/3/library/functions.html#built-in-funcs

print()
print('*'*50)

# Prints all the functions in __builtins__
print(dir(__builtins__)) # -> Prints a list of all the functions

print()
print('*'*50)

# prints all the elements seprately
for i in dir(__builtins__):
    print(i)

print()
print('*'*50)

# Prints all the classes in shelve 
print(dir(shelve))

# Printing all the functions of Shelf object
for obj in dir(shelve.Shelf):
    if obj[0] != '_': # there should be no _ at the 0th position of the string
        print(obj)

#help(shelve)
help(random.randint) # returns random integer including both end points

    

