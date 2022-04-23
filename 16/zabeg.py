from turtle import *
from random import randint

speed(50)
def draw_back(x1, y1, x2, y2, col):
	up()
	color(col)
	goto(x1,y1)
	down()
	begin_fill()
	goto(x2, y1)
	goto(x2, y2)
	goto(x1, y2)
	goto(x1, y1)
	end_fill()
	up()
draw_back(-500, -450, 500, 450, "black")

speed(1)
def start(turtle, x, y, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.shape('turtle')
    turtle.color(color)
    turtle.left(90)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

start(t1, -20, -200, 'pink')
start(t2, 20, -200, 'orange')
start(t3, 60, -200, 'PaleTurquoise')

finish = 200
while t1.ycor() < finish and t2.ycor() < finish and t3.ycor() < finish:
    t1.fd(randint(4,7))
    t2.fd(randint(4,7))
    t3.fd(randint(4,7))

def dance(turtle):
    for i in range(64):
        turtle.left(30)    

if t1.ycor() > t2.ycor() and t1.ycor() > t3.ycor():                               
    dance(t1)
if t2.ycor() > t1.ycor() and t2.ycor() > t3.ycor():                               
    dance(t2)  
if t3.ycor() > t2.ycor() and t3.ycor() > t1.ycor():                               
    dance(t3)             
else:
    dance(t1)
    dance(t2) 
    dance(t3)       
mainloop()