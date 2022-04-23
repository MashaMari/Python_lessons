import tkinter as tk

def on_click():
    global score
    score += 1
    button1.config(text=str(score))
win = tk.Tk()
score = 0
button1 = tk.Button(win, text=str(score), command=on_click, width=30)
button1.pack()
win.mainloop()