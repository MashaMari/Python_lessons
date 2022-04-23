from turtle import *

t = Turtle()

def draw(x, y):
    t.goto(x, y)

t.ondrag(draw)

mainloop()