import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Grid Geometry")
mainWindow.geometry('640x480+360+140')

label = tkinter.Label(mainWindow, text="Learning Grid Geometry")
label.grid(row=0, column=0)

# Creating Left Frame
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

# Placing the canvas in the Left Frame
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth="1")
canvas.grid(row=1, column=0)

# Creating the Right Frame
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

# Creating the buttons
button1 = tkinter.Button(rightFrame, text="Button-1")
button2 = tkinter.Button(rightFrame, text="Button-2")
button3 = tkinter.Button(rightFrame, text="Button-3")
button4 = tkinter.Button(rightFrame, text="Button-4")

#placing the buttons in the frame
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)


# CONFIGURING THE COLUMNS AND GIVING THEM "WEIGHT"
# columnconfigure and grid_columnconfigure and the same. The former points to the latter only
# weight affect the behaviour of the widgets inside them, mainly seen during resizing the window
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)


# CONFIGURING FRAMES AND GRIDS
leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)

leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")


# CONFIGURING COLUMNS OF INDIVIDUAL FRAMES
rightFrame.columnconfigure(0, weight=1)
button1.grid(sticky="ew")
button2.grid(sticky="ew")
button3.grid(sticky="ew")
button4.grid(sticky="ew")

mainWindow.mainloop()
