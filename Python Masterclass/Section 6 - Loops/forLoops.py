"""
Showcasing the For Loops
with keywords like "in" and "len()"
"""

for i in range(1, 20):  # the loop will function till 19 i.e {1 to (n-1)}
    print(i)

NUMBER = "12,44,23,1,222,345,643,887,984"
for i in range(0, len(NUMBER)): # this is sommething i would code in C++/JAVA, for python, see below
    print(NUMBER[i])

for i in range(0, len(NUMBER)):
    if NUMBER[i] in "1234567890":
        print(NUMBER[i], end=' ') # by default, the print() adds new line

# adding all the numbers
# there is a huge difference between + operation for a string
# and a integer. For a string, it concatenates and for a integer it adds
print()
cleanedNumber = ''
for i in range(0, len(NUMBER)):
    if NUMBER[i] in "123456789":
        cleanedNumber = cleanedNumber + NUMBER[i] # cleaned number is a string here

# this is used in extracting out the Phone Numbers, 844-747-8305 -> 8447478305
newNumber = int(cleanedNumber)
print('New Number is {}'.format(newNumber))


# there is a difference between the iterating of for loops of python and of JAVA, C, C++
# this is how i will code for loop in python

num = '844-747-8305'
phoneNumber = ''

for char in num:
    if char in "0123456789":
        phoneNumber = phoneNumber + char

myPhoneNumber = int(phoneNumber)
print('My phone number is {}'.format(myPhoneNumber)) # myPhoneNumber is a int
print('My phone number is '+phoneNumber) # string is concatenated, int cannot

# Printing the tables from 1-13

for i in range(1, 13):
    for j in range(1, 13):
        print('{1} times {0} is {2}'.format(i, j, i*j))
    print('###############') # the indentation of this print is very important



shoppingList = ["milk", "bread", "chocolate"]
for item in shoppingList:
    print('Buy '+item)
