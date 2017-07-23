import tkinter
def printStuff():
    width = 80
    text="this is a practice function"
    left_margin = (width-len(text))//2
    print(" "*left_margin, text)


printStuff()

def center_text(text):
    text = str(text) # because when it recieves 12, we have to conevert it into a string because len() expects a string
    width = 80
    left_margin = (width-len(text))//2
    print(" "*left_margin, text)


center_text("Hi")
center_text("Hi"*2)
center_text("Hi"*4)
center_text("Hi"*6)
center_text("Hi"*8)
center_text(12)

# center_text(12) this will give an error because the function len() is expecting a string and not an int


# MAKING YOUR OWN PRINT FUNCTION USING THE ARGUMENTS OF THE MAIN PRINT FUNCTION
print('-----------MY PRINT FUNCTION----------')

def myPrint(*text, sep=" ", end="\n", file=None, flush=False):
    incomingText =''
    for arg in text:
        incomingText += str(arg) + sep
    
    print(incomingText, end=end, file=file, flush=flush)
    print(locals()) # prints all the local variables of the function



myPrint("aditya", "tyagi", "hello", sep=": ", end="\n")


# CREATING A FUNCTION THAT ALLOWS TO WRITE ON AN EXTERNAL FILE
print()
print('-----------PRINT TO EXTERNAL FILE----------')

def myPrintExternal(*text, sep=" ", end="\n", file=None, flush=False):
    incomingText =''
    for arg in text:
        incomingText += str(arg) + sep
    
    print(incomingText, end=end, file=file, flush=flush)



with open("External.txt", mode="w") as external:
    myPrintExternal("Hi", file=external)
    myPrintExternal("Hi"*2, file=external)
    myPrintExternal("Hi"*3, file=external)
    myPrintExternal("Hi"*4, file=external)
    myPrintExternal("Hi"*5, file=external)


print('print to external file success')



# THE CONCEPT OF RETURNING
print()
print('-------THE CONCEPT OF RETURNING---------')

def family(names):
    names += ' is my brother!'
    return names


fullSentence = family('Ayush')
print(fullSentence)



print(tkinter.TkVersion)






    