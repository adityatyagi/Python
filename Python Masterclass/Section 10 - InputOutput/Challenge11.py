# APPENDING TO THE FILES
# .append() appends to last of the file, without changing the details
# MODE 'a' for append

# Challenge -> append the tables from 2 to 12 to tables.txt

with open('tables.txt', 'a') as tables:
    for i in range(2,13):
        for j in range(1,13):
            print('{1:>2} times {0} is {2}'.format(i,j,i*j), file=tables)
        print('*'*50,file=tables)
