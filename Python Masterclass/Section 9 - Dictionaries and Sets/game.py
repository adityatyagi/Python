locations = {
    0: "You are sitting in front of a laptop and learning Python",
    1: "Road",
    2: "Hill",
    3: "Building",
    4: "Valley",
    5: "Forest"
}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]


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

    direction = input("Available exits are:  "+ available_exits).upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print('You cannot go in that direction')