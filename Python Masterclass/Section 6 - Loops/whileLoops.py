"""
The while loops

The while loops in python are different than for loops in a way that
it is used when we dont know the number of times the code within the loops has
to run

The variable of the while loop condition has to be initialised first

when the condition doesnt follow a sequence - Game (Direction Selection)
the for loop will repeat the code within it in a pre determined sequence
while with the while loop you dont need to know ahead of time the number of times
the loop will be executed

"""

i = 0
while i < 10:
    print(i)
    i += 1


# Game direction

availableDirections = ['east', 'south', 'south-east']

#initailising the condition variable
chosenExit = ''
while chosenExit not in availableDirections:
    chosenExit = input('Please choose another drection: ')
    if chosenExit == 'quit':
        print('Game Over')
        break
else:
    print('You must be glad that you are out now')

# the else clause in while loop works only if there is no break in the while loop execution
# If the else statement is used with a while loop, the else statement is executed when the condition
# becomes false, not when there is a break





