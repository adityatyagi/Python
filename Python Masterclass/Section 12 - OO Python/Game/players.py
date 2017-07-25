'''
This is used to show the property of Getters and setters
'''

'''
getter: it is a method to get the value of the data attribute
getters can be created later, no need to make them initially
setter: sets the value of the data attribute

getters and setters are used with property that uses these getters and setters
_lives have been replaced by lives
'''

class Players(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3 # hiding the lives attribute by using _
        self._level = 1
        self._score = 0
    

    # again, hiding the getters and setters by starting it with _
    def _get_lives(self): 
        return self._lives

    def _set_lives(self, lives): # validation for setting the values of lives
        if lives >= 0:
            self._lives  = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
    

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score = delta * 1000
            self._level = level
        else:
            print('Level cannot be less than 1')
    

    # DECORATORS -> handles the work of making the property
    @property                   # this is the getter as well as the property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


    # getters and setters are used with property
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)