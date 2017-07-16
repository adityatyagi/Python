"""Section 5 for Python: Matserclass Udemy Course"""

print("Hello")
print(4+5)

# Concatenate Strings
HELLO = "Greetings, "
NAME = "Aditya"
print(HELLO + NAME)

# One cannot concatenate strings with integers
AGE = 24
# print("My name is "+name+"and my age is "+age)

# print("My name is "+name+" and my age is "+str(age))
print("My age is {0} and my name is {1}".format(AGE, NAME))




# Taking input form keyboard via input()

GREETING = "Hello"
NME = input(
    "Please enter your name:"
)
print(GREETING +" "+ NME)

# Split String
SPLITSTRING = "This string has been\nsplit into\nnumber of \nlines"
print(SPLITSTRING)

#Tabbed String
TABBEDSTRING = "1\t2\t3\t4\t5"
print(TABBEDSTRING)


# Skipping stuff
print("It was Ginny\'s Choice")

# Tripe """

ANOTHERSPLITSTRING = """This string has been
split over
multiple
lines """
print(ANOTHERSPLITSTRING)


# Variables
A = 10
B = 5
print(A+B)
print(A-B)
print(A*B)
print(A/B) 
print(A//B)
print(A%B)

# ----------Data Types-----------
# Numeric
# Sequence (Strings)
# Mappings
# Files
# Instances
# Classes
# Exceptions

PARROT = "Aditya Tyagi"
print(PARROT)
print(PARROT[0])
print(PARROT[3])

# Used to extract certain characters
print(PARROT[0:4])
print(PARROT[4:])
print(PARROT[:6])
print(PARROT[-1])
print(PARROT[-4:-2])

NUMBERS = "1,2,3,4,5,6,7,8,9"
print(NUMBERS[0::2])

NUMBER = "9,223,372,036,775"
print(NUMBER[1::4])



# Is one string part of another?
TODAY = "friday"
print("day" in TODAY)
print("fri" in TODAY)
print("thur" in TODAY)


# Replacement Fields
print("""    January: {0}
    February: {0}
    March: {2}
    April: {1}
    May: {2}
    June: {1} """.format(28, 30, 31))


# String formatting operator - Depreciated in Python 3
print("My age is %d" % AGE)
print("My age is %d %s, %d %s" % (AGE, "Years", 6, "Months"))


# this will be right formatted
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i**2, i**3)) # ** is for power
print("------------------------------")

#LEFT FORMATTED because of <4
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))
     
print("------------------------------")


print("No {} squared is {} and cubed is {}".format(i, i**2, i**3))




