from tkinter import *
from tkinter.ttk import *
import time


def start():
    gigabytes = 100
    download = 0
    speed = 1
    while download < gigabytes:
        time.sleep(0.05)
        bar['value'] += (speed/gigabytes)*100
        download += speed
        percent.set(str(int((download/gigabytes)*100)) + "%")
        text.set(str(download) + "/" + str(gigabytes) + " GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

button = Button(window, text="download", command=start).pack()
window.mainloop()











