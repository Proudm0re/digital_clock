from cgitb import text
from tkinter import Label, Tk
import tk
import time
global root

root = Tk()
root.geometry("700x300")

# display time on the label

def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text = current_time)
    clock.after(200, timing)

# Styling the label widget

clock = Label(root, font =("calibri", 60, "bold"), bg  = "black", fg = "white")
clock.grid(row=2, column=2, pady=45, padx=100)
timing()

digital= Label(root, text="Ethan's PogO'Clock", font = "calibri 24 bold")
digital.grid(row=0, column=2)

nota= Label(root, text = "hours       minutes       seconds", font = "calibri 15 bold")
nota.grid(row=3, column=2)

root.mainloop()