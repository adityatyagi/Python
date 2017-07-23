#import blackjack
from blackjack import *
# rigth now, the import is directly starting the game, which we dont want
# https://docs.python.org/3/reference/import.html
print(__name__)  # actually, __name__ is name of the module, without any path 
#blackjack.play() 
# rint(blackjack.cards) # this way we can use the deck of cards in other games like teen pati, rummy as well


# will give the same result
#print(locals())
#print(globals())


# dictionary changed size during iteration, because x is added to the dictionary returned by globals() during iteration
# to resolve this we make a quick copy of the dictioary and then iterate through it
#for x in globals():
#    print(x)




g = sorted(globals())
for x in g:
    print(x)