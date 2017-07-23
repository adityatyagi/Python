# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

keys = [
    [('C', 2), ('CE', 2)],
    [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
    [('0', 1), ('=', 1), ('/', 1)]
]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

# Result Box
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky="nsew")


# Frame for KEYPAD
keypadFrame = tkinter.Frame(mainWindow)
keypadFrame.grid(row=1, column=0, sticky="nsew")

# Keypad Numbers
row = 0
for keyRow in keys:
    col=0
    for key in keyRow:
        #Create Button
        tkinter.Button(keypadFrame, text=key[0]).grid(row=row, column=col, colspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1


mainWindow.update()
mainWindow.minsize(keypadFrame.winfo_width() + mainWindowPadding, result.winfo_height() + keypadFrame.winfo_height())
mainWindow.maxsize(keypadFrame.winfo_width()+ 50 + mainWindowPadding, result.winfo_height() + 50 + keypadFrame.winfo_height())

mainWindow.mainloop()