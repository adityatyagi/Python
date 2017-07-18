import shelve

# MANUAL OPEN AND CLOSE
''' fruit = shelve.open('ShelfTest')

fruit['orange'] = "Orange"
fruit['lemon'] = "Lemon"
fruit['apple'] = "Apple"
fruit['grapes'] = "Grapes"

print(fruit['orange'])
fruit.close()

print(fruit)
 '''

# WHILE RUNNING THE PROGRAM, BE VERY CAREFUL BECAUSE THE SHELEVES ARE PERSISTENT DICTIONARIES
# THIS MEANS THAT, IT WILL MAKE COPIES OF THE DATA IF RAN OVER AND OVER AGAIN

# Without MANUAL OPEN AND CLOSE
# INDENTATION MATTERS

with shelve.open('ShelfTest2') as names:
    names['aditya'] = "Aditya"
    names['saksham'] = "Saksham"
    names['anant'] = "Anant"
    names['shubi'] = "Saransh"

    print('aditya')


print(names)


