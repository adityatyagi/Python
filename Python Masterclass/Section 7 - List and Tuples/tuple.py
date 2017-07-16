# tuples are immutable 
# the tuples are used to store data of different kinds data type

t = ("a", "b", 2) # tuple
num = [1,2,3,4,5] # list 

print(t)
print(num)

print("a", "b", "c") # string
print(("a", "b", "c")) #tuples

person1 = ("Aditya Tyagi", 24, "C++")
person2 = ("Sarthak Grover", 23, "JAVA")
person3 = ("Divesh Chaudhary", 12, "Python")

print(person1)
print(person2)
print(person3)

# We cannot directly change the values of the any tuple as the tuple variables are immutable
# but the tuple variables are pointing to the object that stores all the information
# whenever we change the information by a particular syntax, the tuple variable starts pointing to the NEW OBJECT

#person1[0] = "Sanju"       <-- will not work
print('-------------Changed the tuple details-----------')
person1 = "Sanju", person1[1], person1[2]
print(person1)


# but we can directly access the tuple details via []
print(person2[2])


# we can change the details directly of the list items
names = ["aditya", "sarthak", "sanju","vibhu"]
print('Name[2] before change {}'.format(names[2]))
names[2] = "nikhil"
print('Name[2] after change {}'.format(names[2]))


# advantages of tuples over lists
# 1. Security -> can help you avoid bugs
# 2. tuples are INTENDED to store data of various data types but the lsit is INTENDED to store the
#   data of same data type

# Assign multiple variables the same value
a=b=c=d=4
print(a,b)

# UNPACKING THE TUPLE
name, age, language = person2
print(name)
print(age)
print(language)


"""
What will be the status of the tuple if it contains muttable objects like list?
The contents of the tuples cannot be changed, but the contents of the LIST can change



we can unpack the list, but we need equal number of variables

tuple doesnt have an append method

tuples can contain elements that are tuples themselves

use ( ) to ensure individuals tuples
"""

imelda = "More Mayhem", "Imelda May", 2011, [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]

title, artist, year , tracks = imelda
print(title)
print(artist)
print(year)
tracks.append((5, "aditya tyagi"))
print('The tracks are:')
tracks.append((6, 'mishti'))
for songs in tracks:
    # unpacking the songs list
    trackNumber, trackName = songs
    print("\t Track Number: {}, Title: {}".format(trackNumber, trackName))