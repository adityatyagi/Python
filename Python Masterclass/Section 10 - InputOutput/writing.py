# Strip: remives characters only from end and beginning
# also returns partial matches

print("Aditya".strip('A'))

# WRITING TO A FILE AND THEN READING THAT FILE 
imelda = "aditya", "tyagi", ((1, "hello"), (2, "sir")) # TUPLE

with open('write.txt', 'w') as words:
    print(imelda, file=words)


# NOW READING FROM THE SAME FILE
with open('write.txt') as words:
    contents = words.readline()

thisTupple = eval(contents)
print(thisTupple)
# unpacking the tuple
name, surname, extra = thisTupple
print(name)
print(surname)
print(extra)
number, desc = extra
print(number)
print(desc)