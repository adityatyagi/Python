
# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10
ans = random.randint(1, highest) # generates random number
number = 0


while number != ans:
    number = int(input('Enter a number between 1 and 10 and Press 0 to quit:  '))

    if number == 0:
        print('Quit')
        break

    if number < ans:
        print('Guess higher')

    elif number > ans:
        print('Guess Lower')

    else:
        print('You Guessed it')           
            
    