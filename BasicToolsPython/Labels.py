from tkinter import *

window = Tk()

photo = PhotoImage(file='C:\\Users\\beryp\\Desktop\\XDDD.png')

label = Label(window, text="Hello Guys!",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound=TOP)
label.pack()
# label.place(x=0, y=0)


window.mainloop()












