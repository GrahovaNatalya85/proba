from tkinter import *
from tkinter import messagebox as md
from tkinter import  simpledialog as sd
import datetime
import time
import  pygame

t = 0
music = False

def set(mb=None):
    global t
    rem = sd.askstring("Время напоминания", "Введите время напоминания в формате чч:мм" "(в 24 часовом формате)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")

def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")
window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=10)
check()

window.mainloop()