from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor() #assign color to a vraible
    color_hex = color[1]         # assigns element at index 1 to a variable
    window.config(bg=str(color_hex)) #  change background color


window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()

