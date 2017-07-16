"""
Break, Continue and Else - used for breaking out the loop completely and also if 
                           you want to skip the current iteration and move to the next one
"""

# the "break" will give an error if the condition variable goes undefined
# example -> This piece of code will give out an error

shoppingList = ["eggs","ham", "chicken", "milk", "paneer"]
for item in shoppingList:
    if item == "ham":
        nastyFoodItem = item  # it breaks on ham, but if ham is not there in the list, it will give an error 
        break
    print(item)
print("Can\'t i have anything that has "+nastyFoodItem)
print('##########')
for item in shoppingList:
    if item == "milk":
        print('I have skipped '+ item)
        continue # will skip milk
    print(item)

# break and continue are used in Search operations when there are a large number of items in the list

# to tackle this problem of missing ham, in break or continue, define the variable before to empty string
# taking the break example

nastyFood = ''
shopping = ['jeans', 'clothes', 'gel']
for item in shopping:
    if item == 'food':
        nastyFood = item 
        break               # this break doesnt give an error, even though food is not present in the list
    print('The shopping list contains '+item)

if nastyFood == 'food':
    print('I promise i wont have '+nastyFood)






# else is used with "for" as well as with "if" in python, therefore be very carefull with the indentation

# WORKING OF ELSE WITH FOR
# the "else" block of code runs, if the control flow didnt go out of the for loop

nonVeg = ''
meal = ['roti', 'chappati', 'rice', 'omellete', 'milk']
for itemm in meal:
    #print('The meal contains '+itemm)
    if itemm == 'omellete':
        nonVeg = itemm
        break
# incase, omellete is not present in the list
else:
    print('The meal contains '+itemm)

if nonVeg == 'omellete':
    print('I ordered a veg meal.')

"""
If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.
"""

# Prime Numbers between 10 to 20

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0: # first factor
            j = num // i  # second factor, changing to float if single division / is used (num / i)
            print('{0} equals to {1}*{2}'.format(num,i,j))
            break # break to the FIRST FOR LOOP
    else:
        print('{0} is a prime number'.format(num))