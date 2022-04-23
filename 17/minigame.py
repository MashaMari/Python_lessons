from turtle import *

t = Turtle()
t.color('Indigo')
sp = 10

def go_w():
    t.goto(t.xcor(), t.ycor() + sp)

def go_s():
    t.goto(t.xcor(), t.ycor() - sp)  

def go_a():
    t.goto(t.xcor() - sp, t.ycor())    

def go_d():
    t.goto(t.xcor() + sp, t.ycor())  

scr = t.getscreen()
scr.onkey(go_w, 'w')
scr.onkey(go_s, 's')
scr.onkey(go_a, 'a')
scr.onkey(go_d, 'd')

scr.listen()

mainloop()