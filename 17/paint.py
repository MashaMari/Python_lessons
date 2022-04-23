from turtle import *

t = Turtle()
t.color('red')
t.width(5)
t.shape('circle')
t.down()
t.speed(10)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def set_red():
    t.color('red')

def set_green():
    t.color('green')

def set_blue():
    t.color('blue')  

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(set_red, 'r')
scr.onkey(set_green, 'g')
scr.onkey(set_blue, 'b')

scr.listen()
mainloop()