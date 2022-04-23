import turtle
import random

t = turtle.Turtle()
scr = turtle.Screen()

colors = ['green', 'red', 'blue', 'orange']

a = 0
while a < 4:
    t.color(random.choice(colors))
    t.forward(100)
    t.left(90)
    a += 1

scr.exitonclick()    