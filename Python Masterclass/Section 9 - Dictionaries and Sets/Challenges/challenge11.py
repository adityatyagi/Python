# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

sampleText = "My name is Aditya Tyagi"
vowels = frozenset("aeiou")
sampleSet = set(sampleText).difference(vowels)
print(sampleSet)

finalList = sorted(sampleSet)
print(finalList)