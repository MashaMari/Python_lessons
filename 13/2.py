from turtle import *

up()
goto(-100, 0)
down()

def triugolnik():
    for i in range(3):
        fd(100)
        left(120)
triugolnik() 
fd(100)
up()
goto(50, 0)
down()

triugolnik()

fd(100)
up()
goto(200, 0)
down()

triugolnik()
input()