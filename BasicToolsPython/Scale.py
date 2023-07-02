from tkinter import *


def submit():
    print("The temperature is " + str(scale.get()) + " degrees")


window = Tk()


scale = Scale(window, from_=0,
              to=100,
              length=600,
              orient=HORIZONTAL,
              font=("Consolas", 20),
              tickinterval=10,
              #showvalue=0
              resolution=5,
              troughcolor="#69EAFF")
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()













