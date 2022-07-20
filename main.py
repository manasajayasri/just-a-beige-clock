import string
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("The beige Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)

lable = Label(root, font=("ds-digital", 80), background="brown", foreground= "beige")
lable.pack(anchor='center')
time()

mainloop()