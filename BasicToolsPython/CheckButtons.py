from tkinter import *


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

x = IntVar()

furby_photo = PhotoImage(file='C:\\Users\\beryp\\Desktop\\XDDD.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           activeforeground="#00FF00",
                           bg="black",
                           activebackground="black",
                           padx=20,
                           pady=15,
                           image=furby_photo,
                           compound=LEFT)
check_button.pack()

window.mainloop()











