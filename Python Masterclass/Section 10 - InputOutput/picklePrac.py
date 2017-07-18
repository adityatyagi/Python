# using pickle to write and read binary data
# there are two methods .load() and .dump()
# Python provides a mechanism for serialising objects called Pickling

import pickle

bio = (
    'aditya',
    'tyagi',
    '2000',
    ((1, 'Hunny'),
    (2, 'Money'),
    (3, 'Jolly'))
)

even = list(range(0,20,2))
odd = list(range(1,20,2))

# write
with open('pickleFile', 'bw') as pickle_write:
    pickle.dump(bio, pickle_write)
    pickle.dump(10021996, pickle_write)
    pickle.dump(even, pickle_write) # protocol=pickle.HIGHEST_PROTOCOL 
    pickle.dump(odd, pickle_write)

# read
with open('pickleFile', 'br') as pickle_read:
    bioCopy = pickle.load(pickle_read)
    randomNumber = pickle.load(pickle_read)
    evenList = pickle.load(pickle_read)
    oddList = pickle.load(pickle_read)

print(bioCopy)

# Unpacking the tuples
name, surname, year, others = bioCopy
print(name)
print(surname)
print(year)
print(others)

print(randomNumber)
print(evenList)
print(oddList)