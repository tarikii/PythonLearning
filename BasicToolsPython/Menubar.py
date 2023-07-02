from tkinter import *


def open_file():
    print("You opened a file!")


def save_file():
    print("You saved a file!")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You paste some text!")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

file_photo = PhotoImage(file="file.png")
save_photo = PhotoImage(file="save.png")
exit_photo = PhotoImage(file="exit.png")

file_menu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=file_photo, compound=LEFT)
file_menu.add_command(label="Save", command=save_file, image=save_photo, compound=LEFT)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_photo, compound=LEFT)

edit_menu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
window.mainloop()










