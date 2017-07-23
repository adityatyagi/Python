
personal_details = ("aditya", "24", "tyagi") # tuple

# unpacking the tuple
name, _, surname = personal_details
print(name)
print(_) # underscore can be used as a THROW-AWAY VARIABLE
print(surname)

# THROWAWAY VARIABLE:
# a variable that we wouldnt be using any more than once, its not that useful

'''
python doesn't have any concept of private and protected variables

we can use the _ for setting up our own variables with the same name as the python has
e.g from_=0, to=59 in setting the range



try to avoid using the _variables of other's code


_deal_card made it a protected member, though we still have access to it, beacuse we imported directly not not using *


if we import using the *, we import all the variables and then we can use it as our own, therefore it is advised to avoid using it

with *, everything in the blackjack module namespace, appears in our module namespace
python will not import _variables when you import using *

invoking anything with __ () double underscores runs the python name mangling rules

'''