# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year , tracks = imelda
print(title)
print(artist)
print(year)
print('The tracks are:')
for songs in tracks:
    # unpacking the songs tuples
    trackNumber, trackName = songs
    print("\t Track Number: {}, Title: {}".format(trackNumber, trackName))


# it would be a better option to store the albums in list, because when new album comes, 
# you can append it aling with the year



