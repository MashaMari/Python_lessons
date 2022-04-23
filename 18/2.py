import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text='Click on me', command=on_click)
button1.pack()
win.mainloop()