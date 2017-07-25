'''
getter: it is a method to get the value of the data attribute
getters can be created later, no need to make them initially
setter: sets the value of the data attribute

getters and setters are used with property that uses these getters and setters
_lives have been replaced by lives
'''

from players import Players # this kind of importing must be avoided
from enemy import Enemy, Troll, Vampyre, VampyreKing

aditya = Players("Aditya")

# print(aditya.name)
# print(aditya.lives)
# print(aditya.__dict__)

''' aditya.lives -= 1
print(aditya)

aditya.lives -= 1
print(aditya)

aditya.lives -= 1
print(aditya)

aditya.lives -= 1
print(aditya) '''


# aditya.level = 5 # level - _level
# print(aditya)

# aditya.score = 500
# print(aditya)

random_monster = Enemy('Basic Enemy', 12, 1)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

# this is the final hit the monster can take, on taking, it looses 1 life
random_monster.take_damage(1)
print(random_monster)


# This also shows an example of Overloading and Subclassing
# Overloading: same name, different arguments, or different signature

troll1 = Troll('Troll-1') # will take the init method of its superclass Enemy with default arguments's value
print(troll1)

troll2 = Troll('Troll-2')
print(troll2)

troll3 = Troll('Troll-3')
print(troll3)

troll1.grunt()
troll2.grunt()

troll1.take_damage(4)
print(troll1)

troll1.take_damage(20)
print(troll1)

troll2.take_damage(20)
print(troll2)

troll2.take_damage(2)
print(troll2)

troll2.take_damage(1)
print(troll2)

troll2.take_damage(1)
print(troll2)

# troll2.take_damage(4)
# print(troll2)

print('------------------------')

# Creating Vampyre instances
vam1 = Vampyre('vam1')
print(vam1)

vam2 = Vampyre('vam2')
print(vam2)

vam1.take_damage(5)
print(vam1)

vam1.take_damage(8)
print(vam1)

vam3 = Vampyre('vam3')
print(vam3)

while vam3._alive:
    vam3.take_damage(1)
    print(vam3)



print('---------Vampyre King---------')
dracula = VampyreKing('Dracula')
print(dracula)
dracula.take_damage(12)
print(dracula)