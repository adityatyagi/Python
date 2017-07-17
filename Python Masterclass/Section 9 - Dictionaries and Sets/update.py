# update and copy dictionaries
# on update, a new dict is not created, the same one is updated

locations = {
    0: "You are sitting in front of a laptop and learning Python",
    1: "Road",
    2: "Hill",
    3: "You are in the, building",
    4: "Valley",
    5: "Forest"
}


directions = {
    6: "North",
    7: "East",
    8: "West",
    9: "South"
}

print(locations)
print(directions)

# .update() doesn't return anything, like .sort()
# print(locations.update(directions)) will not work

locations.update(directions)
print(locations)

# copying the dict to make a brand new dict
newDict = locations.copy()
print(newDict)

newElements = {
    'name': "Aditya",
    'age': "21",
    'branch': "IT"
}

newDict.update(newElements)
print(newDict)

print(locations) # No harm is done to locations dict