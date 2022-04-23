from tkinter import *
import random

def from_rgb(rgb):
    return '#%02x%02x%02x' % rgb

def change_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    button.config(bg=from_rgb((r, g, b)))

window = Tk()
window.title('1')
button = Button(window, text='CLICK', command=change_color)
button.grid(column=0, row=0)
window.mainloop()