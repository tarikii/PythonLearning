from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="This is an info messagebox", message="You are a person")
    # messagebox.showwarning(title="WARNING!", message="YOU HAVE A VIRUS!!!!!")
    # messagebox.showerror(title="ERROR!", message="SOMETHING WENT WRONG!")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #    print("You did the thing!")
    # else:
    #    print("You cancelled the thing! :(")

    # if messagebox.askretrycancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #    print("You retried the thing!")
    # else:
    #    print("You cancelled the thing! :(")

    # if messagebox.askyesno(title="ask yes or no", message="Do you like cake?"):
    #    print("I like cake too :)")
    # else:
    #    print("Why do you not like cake? :(")

    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")

    # if answer == "yes":
    #    print("I like pie too :)")
    # else:
    #    print("Why do you not like pie? :(")

    answer = messagebox.askyesnocancel(title="yes no cancel", message="Do you like to code?")
    if answer:
        print("You like to code :)")
    elif answer is False:
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")


window = Tk()

button = Button(window, command=click, text="Click me!")
button.pack()

window.mainloop()
