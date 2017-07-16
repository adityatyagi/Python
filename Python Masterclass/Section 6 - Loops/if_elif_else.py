"""
Showcasing examples practiced for if-elif-else
"""
# Example 1
NAME = input('Please enter your name')
AGE = int(input('Please enter your age, {}'.format(NAME)))

if AGE < 18:
    print('You are not allowed to vote')
    print('Come after {} years'.format(18-AGE))
else:
    print('You are allowed to vote')

print('-----------------------------------------------')

# Example 2
print('Please guess a number between 1 and 10')
guess = int(input())

if guess < 5:
    print('Please guess higher')
    guess = int(input())
    if guess == 5:
        print('You guessed it.')
    else:
        print('Sorry, wrong guess.')
elif guess > 5:
    print('Guess a lower value')
    guess = int(input())
    if guess == 5:
        print('You guessed it right')
    else:
        print('Sorry, wrong guess')
else:
    print('you guessed it in the first go.')

print('-----------------------------------------------')

# Example 3: Example 2 had a lot of repeated code. Therefore we ca make it shorter

print('Please guess a number between 1 and 10')
guess = int(input())

if guess != 5:
    if guess < 5:
        print('Guess higher')
    else:
        print('guess lower')
    guess = int(input())
    if guess == 5:
        print('You guessed it')
    else:
        print("Sorry, wrong guess")

print('--------------------------------------------------')

# AND
NUM = int(input('Enter any number'))

if  (NUM > 0) and (NUM < 100):
    print("The number is between 0 and 100")
else:
    print('The number is above 100 or less than 0')

print('--------------------------------------------------')

# OR
NUM = int(input('Enter any number'))

if  (NUM < 0) or (NUM > 100):
    print("The number is above 100 or less than 0")
else:
    print('The number is between 0 and 100')

print('--------------------------------------------------')

# IN

STUDENT = "Aditya Tyagi"
LETTER = input("Enter a letter")
print(LETTER)

if LETTER in STUDENT:
    print("The letter {0} is present in the word".format(LETTER))
else:
    print("The letter isn\'t present")

print('----------------------------------------------------')

# NOT

print(not True)
print(not False)
print('#########################')

NUMB = int(input("Enter your age"))
if not(NUMB<18):
    print('You are allowed to vote')
else:
    print('You are not allowed to vote')


print('--------------------------------------------------------')

# True / False

x = "false"
if x:
    print('x is true')

print('######################')



