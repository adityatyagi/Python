# there are 6 types of list
# examples of methods with lists

parrotList = ["this", "is", "a", "element", "in", "a", "list"]
parrotList.append("Aditya Tyagi")
for item in parrotList:
    print(item)

# playing with two lists
list1 = [88,2,5,44,55,4]
list2 = list1 # the list2 points to the same memory location as list1
print(list2)

list1.sort()
print(list1)
# print(list1.sort()) -> this doesn't work

list3 = [45,77,8,9,44,12,54,63,4]


print(sorted(list3, reverse=True)) 

# checking the equality of the two lists
list4 = [7,8,9,10]
list5 =list4
print(list5 is list4) #true/false

# any change made to list5, makes the changes to the list4, becuase they are pointing to the same list
list5.sort(reverse=True) #make changes to the list here only, make changes to the original list, returns nothing
print(list5)

if list5 == list4:
    print('they are equal')
else:
    print('theya are not equal')

list6 = [77,88,99,101,1,5,4]
list7 = sorted(list6, reverse=True)
print(list7 is list6)
print(list6)
print(list7) #while comparing, the order and the elements both matter

# all the characters in the list(string) are itterable



#concatenating lists

list8 = list6+list7
print(list8)


#empty list
list10 = []
list11 = list() # list constructor
printListItems = list("Aditya")
print(printListItems) # prints seprate elements of the list

list12 = [list6, list7]
print(list12)

for item in list12:
    print(item)
    for innerValue in item:
        
        print(innerValue)


#iterators
# the for() creates iter() explicitly

numbers = [1,2,3,4,5,6,7,8,9,0]

myIter = iter(numbers)
print(myIter)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# the same thing can be done by
print('#####################')
for itr in numbers:
    print(itr)


# _______________ RANGES and RANGE SLICING ________________

# in python2, the range was a built in data type but in python3, it is a built in function
# for range(n) <- it travers from 0 to (n-1)
"""
range(start,end,jump)
efficient in memory


my_range = range(0, 1000)
new_range = my_range[3: 40: 2]
 
print(my_range)
print(new_range)
print(range(3, 40, 2))
we get the output

range(0, 1000)
range(3, 40, 2)
range(3, 40, 2)
so as you say, they are the same. Let's change my_range

my_range = range(0, 1000, 5)
new_range = my_range[3: 40: 2]
 
print(my_range)
print(new_range)
print(range(3, 40, 2))
and now the output is

range(0, 1000, 5)
range(15, 200, 10)
range(3, 40, 2)
so the slice [3: 40: 2] is slicing a range that goes up in steps of 5, and we get a completely different result.

If you check the values in my_range

for x in new_range:
    print(x)
we get 15 to 195 in steps of 10.

We can also use a slice to reverse the order

for x in new_range[::-1]:
    print(x)


"""


myList = list(range(10))
print(myList)

odd = list(range(1,10,2))
even = list(range(0,10,2))

print(odd)
print(even)



# p2:xrange() and in p3: range()

# the two ranges (0,100000,2) and (0,100,2) takes the same amount of memory

myString = "abcdefghijklm"
print(myString.index('e'))
print(myString[4])


small_decimals = range(0, 10)
print(small_decimals)

for i in small_decimals:
    print(i) # 0 1 2 3 4 5 6 7 8 9  <- on index(3), 3 is present

print(small_decimals.index(3))


oddRange = range(1,10000,2)
print(oddRange)
print(oddRange[985])

# to check if a number entered by user between 1 and 10000 is divisible by 7 or not
sevens = range(7,10000,7)
x = int(input("Please enter a number less than 100000:  "))
if x in sevens:
    print('{} is divisible by 7'.format(x))
else:
    print('{} is not divisible by 7'.format(x))


# RANGE SLICING
print('The range of small decimals is {}'.format(small_decimals))
myRange = small_decimals[::2] # takes the value of small_decimals by default
print(myRange)

for i in myRange:
    print(i)
print('*' *40)
print(myRange[1])
print(myRange.index(8)) # .index(obj) returns the index of the obj

print('*' *40)
decimals = range(0, 100)
print(decimals)

myrange = decimals[3:40:3] # range-sliced
print(myrange)

for item in myrange:
    print(item)

print('*' *40)
# the above sliced range can be represented by:
for item in range(3,40,3):
    print(item)

#while checking the equality of the ranges, we check the result of the ranges and not the numbers
print(range(0,5,2) == range(0,6,2))

print(list(range(0,5,2)))
print(list(range(0,6,2)))
print('*' *40)
# some more examples on Ramge slicing -> NEGATIVE SLICING
r = range(0,100)
print(r)

for i in r[::-2]:
    print(i)

print('*' *40)

for i in range(99, 0, -2):
    print(i)

print('*' *40)

print(range(0,100)[::2] == range(0,100,2))

print('-'*60)

backwardString = 'aytidA'
print(backwardString[::-1]) # because all of the strings elements are iterrable



