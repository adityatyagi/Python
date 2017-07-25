# OBJECT ORIENTATED PYTHON

# till now we have been using imperative style of programming, and not object orientated style of programming
# everything in python is an object
# python supports multiple programmming paradigms
# even types are implemeted as classes
# object orientated programming uses classes and methods to provide that encapsulates both data and the functions that
# operate on that data
# DIFFERENCE BETWEEN FUNCTIONS AND METHODS - When a function is a part of a class, it is a method, also the self parameter
# CLASS: can be a template from which the objects can be created


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle(2014, 250)
print(kenwood)
print(kenwood.make)
print(kenwood.price)

hamilton = Kettle(2017, 500)
print(hamilton)
print(hamilton.make)
print(hamilton.price)

print()
print('----------')
print('{}:{}, {}:{}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price)) 




'''
INSTANCES, CONSTRUCTORS AND MORE...

1. We can specify the attributes of the objects of the instances of the classes in the replacement fields
2. class = type and in python every TYPE is a CLASS 
3. attribute is a variable that is bound to instance of a class
4. Python style guide = pep8
5. self - it is a reference to the instance of the class (its like the "this" keyword in JS)
6. Constructor: a special function which runs when instacne of a class is created, or when a class is instantiated
7. when the method is called directly from the class, the value of self is mandatory
8. Classes in python are dynamic and they can be modified after they are created 
'''

class MyIntro(object):

    def __init__(self, name, midname, surname):
        self.name = name
        self.midname = midname
        self.surname = surname
        self.on = False
    
    def professional(self):
        self.on = True


aditya = MyIntro('aditya', 'NA', 'tyagi')
ayush = MyIntro('ayush', 'NA', 'tyagi')

# print('Aditya: {0.name}-{0.midname}-{0.surname}'.format(aditya))
print('Aditya: {0.name}-{0.midname}-{0.surname}\nAyush: {1.name}-{1.midname}-{1.surname}'.format(aditya, ayush))

print()
print('----------------------------')

print(aditya.on)
aditya.professional()
print(aditya.on)

print()
print('----------------------------')

# accessing directly from the class
print(ayush.on)
MyIntro.professional(ayush)
print(ayush.on)

# Different ways of accessing the class methods by the instances
# MyIntro.professional(ayush)
# ayush.professional()

print()
print('----------------------------')

# the class is dynamic in nature - adding attribute to a instance
aditya.height = '5"8' # height is a INSTANCE VARIABLE
print(aditya.height)

# print(ayush.height)      -> will not work because heght attribute is only attachted to insatnce aditya 

print()
print('------------CLASS ATTRIBUTES----------------')

'''
1. Subclassing: A new class is made from an existing one
2. We can make classes in a way that prohibits the making of additional attributes
3. all instances share the single version of the class attributes
4. when the attribute is asked by the program, the program first checks it in the instances namespaces,
   and once it doesn't find there, it checks the namespaces of the class itself
5. when we assign a new value to a global variable, python assigns the value and makes it a local variable that shadows the global one

'''


"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""


print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)

print()

print('Changing the class attribute from the class')
Kettle.power_source = "atomic"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)

print()
print('Changing the value of class attribute for one particular instance') # this makes it a instance variable (local), which shadows the global one
Kettle.power_source = "atomic"
kenwood.power_source = "nuclear"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)


print()

print('Dictionary')

print(kenwood.__dict__)
print(hamilton.__dict__)
print(Kettle.__dict__)
