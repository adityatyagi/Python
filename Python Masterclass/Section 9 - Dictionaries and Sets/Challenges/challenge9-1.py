# HERE WE ENHANCHE THE GAME using COPY AND UPDATE



# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {
    0: "You are sitting in front of a laptop and learning Python",
    1: "Road",
    2: "Hill",
    3: "You are in the, building",
    4: "Valley",
    5: "Forest"
}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {
    1: {'2': 2, '3': 3, '4': 4, '5': 5},
    2: {'5': 5},
    3: {'1': 1},
    4: {'1': 1, '2': 2},
    5: {'2': 2, '1': 1}
}

vocab = { "QUIT" : "Q",
          "NORTH": "N",
          "SOUTH": "S",
          "EAST": "E",
          "WEST": "W",
          'ROAD': "1",
          'HILL': "2",
          'BUILDING': "3",
          'VALLEY': "4",
          'FOREST': "5"   }

#    print(locations[0].split()) # default delimiter is space ' '
#    print(locations[3].split(",")) # , is a delimiter, the string will split from this ,
#    print(' '.join(locations[0].split(' ')))

# starting at location 1: Road
loc = 1

while True:
    #available_exits = ""
    #for direction in exits[loc].keys():
    #   available_exits += direction + ', '

    available_exits = ', '.join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are:  "+ available_exits+' :').upper()
    print()

    # Parse the user input if necessary - Method 1
    #if len(direction) > 1: # if the user input contains more than one characters
    #    for words in vocab: # iterate through all the keys in vocab
    #        if words in direction: # iterate through all the words in the user input and if vocab[words] == direction[words]
    #            direction = vocab[words]
    


    # Parse the user input if necessary - Method 2
    if len(direction) > 1: # if the user input contains more than one characters
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]
                break


    if direction in allExits:
        loc = allExits[direction]
    else:
        print('You cannot go in that direction')