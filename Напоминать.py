from cProfile import label
from tkinter import *
from tkinter import messagebox as md
from tkinter import  simpledialog as sd
import datetime
import time
import  pygame
from pygame import BUTTON_X1

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание")
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

window.mainloop()