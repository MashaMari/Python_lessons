import tkinter as tk
from tkinter import font as tkFont

def on_click():
    score = int(button1.cget('text')) + 1
    button1.config(text=str(score))
win = tk.Tk()
score = 0
helv36 = tkFont.Font(family='Helvetica', size=72, weight='bold')
button1 = tk.Button(win, text=str(score), command=on_click, width=30, height=7, font=helv36)
button1.pack()
win.mainloop()