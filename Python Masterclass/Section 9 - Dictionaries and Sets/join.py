# strings are immutable, therefore every time the loops runs, a new string is created
myList =['a', 'b', 'c', 'd']
conString = ''
for item in myList:
    conString += item + ', '

print(conString)


# therefore to overcome this problem we use .join()

newString = ','.join(myList)
print(newString)