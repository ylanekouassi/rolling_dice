#ROLLING DICE

from tkinter import *
import random

window = Tk()
window.geometry("500x250")
window.title("Rolling Dice")

button = Button(window, text="ROLL !!!", width=20, height=3, font=50, bg="white", bd=2)
button.pack(padx=10, pady=10)

window.mainloop()
