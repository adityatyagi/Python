''' import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test() '''

try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+360+150') # 360 and 150 are the margins of the mainWindow. It decides the poisition it takes when the app is launched

mainWindow.mainloop()  # helps the program to stay in place till the time it is closed explicitly

