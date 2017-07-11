
"""In python, the augmented assignment evaluates the assignee only once
in others, the variable is evaluated more than once.

a = a + b <- here, a new copy of "a" is made evaluated and destroyed every time, time and memory wastage
a += b <- augmented assignment, the operation is performed in the place itself


"""

x = 10
x += 12
print(x)

x -= 1
print(x)

x *= 100
print(x)

x //= 12                # gives integer after division    
print(x)

x /= 12                 # changes to float
print(x)