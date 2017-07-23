try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# function for a basic parabola
def parabola(page, size):
    for x in range(size):
        y = (x * x) /size # we have divided by 100 to plot the points closer to each other
        plot(page, x, y)  # -y because the graph is upside down and we had to invert the result 
        plot(page, -x, y) # because a parabola is symmetrical along the y axis, we calculate the result for one side and plot it twice, rather than calculating for both the sides
    


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin)) # shifting the origin to the center
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(x, -y, x+1, -y+1, fill="red") # creating the parabola


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)
# draw_axes(canvas2)

parabola(canvas, 100)
parabola(canvas, 300)


mainWindow.mainloop()