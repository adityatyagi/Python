# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

numbers = [1,2,3,4,5,43,56,78,12,34,454,6677,9,80]
sortedNumbers = sorted(numbers)


length = len(numbers)
print('The length of the list is {}'.format(length))

myItr = iter(sortedNumbers)

for item in range(0, length):
    nextItem = next(myItr) # next() returns something
    print(nextItem)
