from tkinter import Tk
from tkinter import Label
import time
import sys

clock=Tk()
clock.title("digital_clock")
def get_time():
    timeVar=time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(clock, font=("DS-Digital", 90), bg="black", fg="skyblue")
clock.pack()
get_time()
clock.mainloop()


