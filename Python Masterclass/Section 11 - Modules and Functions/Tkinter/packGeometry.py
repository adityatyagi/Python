# USE THE CANVAS WIDGET
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Pack Geometry")
mainWindow.geometry('640x480+360+140')

# ----------------LABEL-------------------------
label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side="top")


#---------------------FRAMES----------------------
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", fill=tkinter.Y, expand=False, anchor="n")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", expand=True, anchor="n")


# -------------------CANVAS-------------------
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth="1")
canvas.pack(side="left", anchor="n")


# -------------BUTTONS-----------------------

# Creating Buttons
button1 = tkinter.Button(rightFrame, text="Button-1")
button2 = tkinter.Button(rightFrame, text="Button-2")
button3 = tkinter.Button(rightFrame, text="Button-3")

# Displaying buttons
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")







mainWindow.mainloop()