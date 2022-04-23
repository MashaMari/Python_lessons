from turtle import*

color('blue')

def draw_cube():
    for i in range(4):
        forward(100)
        left(90)

draw_cube()
up()
forward(200)
down()
draw_cube()
input()        
