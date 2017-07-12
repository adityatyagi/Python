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


