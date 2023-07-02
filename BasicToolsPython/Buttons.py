from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()
photo = PhotoImage(file='C:\\Users\\beryp\\Desktop\\XDDD.png')

button = Button(window, text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground="#00FF00",
                state=ACTIVE,
                image=photo,
                compound=BOTTOM)
button.pack()

window.mainloop()















