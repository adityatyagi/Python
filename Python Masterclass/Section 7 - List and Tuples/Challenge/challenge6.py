"""
CHALLENGE 6
"""
# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p: # range of p(0,100,20)
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

r = range(0,50,3)
print(r)
for i in r:
    print(i)

newr = r[::5] # r(0,51,15)
print(newr)











for i in newr:
    print(i)