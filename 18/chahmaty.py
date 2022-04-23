import tkinter as tk

win = tk.Tk()

for j in range(5):
    for i in range(3):
        label = tk.Button(win, text=f'{i}', width=10, bg='orange', fg='white')
        label.grid(row = j, column = i*2 + j % 2)
win.mainloop()    