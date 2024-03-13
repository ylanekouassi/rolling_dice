#ROLLING DICE

from tkinter import *
import random

window = Tk()
window.geometry("500x250")
window.title("Rolling Dice")

label = Label(window, text="", font=("times", 150))
def dice():
    dice = ["\u2680","\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    label.configure(text=f"{random.choice(dice)}")
    label.pack()

button = Button(window, text="ROLL !!!", width=20, height=3, font=50, bg="white", bd=2, command=dice)
button.pack(padx=10, pady=10)




window.mainloop()
