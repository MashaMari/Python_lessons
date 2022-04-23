from turtle import *

turtle1 = Turtle()
turtle2 = Turtle()
turtle1 = shape('turtle')
turtle2 = shape('circle')
turtle1.color('blue')
turtle2.color('red')


turtle1.right(180)

for i in range(5):
    turtle1.fd(100)
    turtle2.fd(100)
    turtle1.right(144)
    turtle2.right(-144)
mainloop()