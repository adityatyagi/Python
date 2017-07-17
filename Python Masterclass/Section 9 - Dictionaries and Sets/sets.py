# creating sets in different ways

# 1. Using the set literal
animals = {"dog", "cat", "sheep"} # this will not have any key-value pairs
print(animals)

for i in animals:
    print(i)

# 2. Using the inbuilt set() function
wild_animals = set(["lion", "leopard", "aditya"])
print(wild_animals)

for i in wild_animals:
    print(i)

print("*"*50)

# adding items to the sets .add()
animals.add('sheep')
wild_animals.add('Money')
print(animals)
print(wild_animals)

print("*"*50)

# we cannot create an empty set with set literal {}, this will create a empty dict
# we donot supply a key, which differentiates it from a dict

# Creating sets from a tuple
animal_tuple = ("elephant", "tortoise", "hare")
tuple_set = set(animal_tuple)
print(tuple_set)

print("*"*50)


# UNION
even = {1,2,3,4,5}
print(even)
print(len(even))
odd = {6,7,8,9,10,1,2,3,4,5}
print(odd)
print(len(odd))
print(even.union(odd))
print(len(even.union(odd)))




# INTERSECTION
print(even.intersection(odd))
print(len(even.intersection(odd)))
print('The other way to print intersection is:')
print(even & odd)



# DIFFERENCE
print(sorted(odd.difference(even))) # if there is no difference -> Null set {} and on sorted({}) -> []
print(sorted(odd - even))

# forzenset
vowels = frozenset("aeiou")
# this is an immuatble set, it can become the keys for the dictionary


# IN-PLACE difference
numbers = {1,2,3,4,5}
num = {2,3}
numbers.difference_update(num) # no new set is formed
print(numbers)

num2 = {4,12,3}
# symmetric difference
numbers.symmetric_difference(num2)
print(numbers)

# symmetric_difference is opposite of intersection
# symmetric differecne - common elements ko chord kr sab kuch

# remove items from set
# .remove(), .discard()
num3 = {55,6,77,89,99,12,2}
print(num3)
num3.remove(55)
print(num3)
num3.discard(89)
print(num3)
num3.discard(90) # will not show an error 
# num3.remove(90) ----> will show an error, therefore check for this number before .remove()


# exception handling
try:
    num3.remove(90)
except:
    print('Not a number')


# subest and superset
num4 = {1,2,3,4}
num5 = {3,4}
if num4.issuperset(num5):
    print("num4 is superset of num5")

if num5.issubset(num4):
    print('num5 is a subset of num 4')

