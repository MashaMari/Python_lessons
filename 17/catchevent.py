from turtle import *
from random import randint

def run_away(x,y):
    w, h = screensize()
    t.goto(randint(-w, w), randint(-h, h))

t = Turtle()
t.onclick(run_away)
# t.speed(0)
# for i in range(1000):
#     run_away(1,1)

mainloop()