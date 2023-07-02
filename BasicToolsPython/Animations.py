from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
x_velocity = 5
y_velocity = 3

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_space = PhotoImage(file="space.png")
space = canvas.create_image(0, 0, image=photo_space, anchor=NW)

photo_ufo = PhotoImage(file="ufo.png")
ufo = canvas.create_image(0, 0, image=photo_ufo, anchor=NW)

ufo_width = photo_ufo.width()
ufo_height = photo_ufo.height()

while True:
    coordinates = canvas.coords(ufo)
    print(coordinates)
    if coordinates[0] >= WIDTH-ufo_width or coordinates[0] < 0:
        x_velocity = -x_velocity
    if coordinates[1] >= WIDTH-ufo_height or coordinates[1] < 0:
        y_velocity = -y_velocity
    canvas.move(ufo, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()








