# METHOD 1 TO OPEN THE FILE, WHERE WE EXPLICITLY OPEN AND CLOSE THE FILE
# file opened
jabber = open('read.txt', 'r') # r is the read mode

for line in jabber:
    print(line, end='') # end='' omits the extra nextline that print introduces

# file closed
jabber.close()

print()
print('*'*50)

# METHOD 2 TO OPEN THE FILE, we dont have to close the file explicitly

with open('read.txt', 'r') as newText:
    for line in newText:
        print(line, end='')

print()
print('*'*50)

# READING LINE - BY - LINE using the readLine()

with open('read.txt', 'r') as newLine2:
    line = newLine2.readline() # Read until newline or EOF
    while line:
        print(line, end='')
        line = newLine2.readline()


# .read() -> will continuously read the data over and over again
# there is also a difference between
# 1. .readlines()
# 2. .readline()
# 3. .read()




