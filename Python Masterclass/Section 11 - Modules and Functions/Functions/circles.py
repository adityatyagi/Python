try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_oval.html
# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_oval-method



mainWindow = tkinter.Tk()
mainWindow.title("Circle")
mainWindow.geometry('640x480')


def circle(page, radius, g, h, color="red"):
    page.create_oval(g-radius, h-radius, g+radius, h+radius, outline=color, width=2)

# create the axes
def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

circle(canvas, 100, 100, 100, 'green')
circle(canvas, 100, -100, -100, 'yellow')
circle(canvas, 100, 100, -100, 'red')
circle(canvas, 100, -100, 100, 'black')



mainWindow.mainloop()