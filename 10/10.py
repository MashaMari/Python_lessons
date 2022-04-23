from turtle import *

# Функция отвечает за цвет черепашки
color("green")

#red, orange, yellow, green, blue, purple, black, white

forward(100)
left(90)

# Функция отвечает за ширину черепашки
width(5)

forward(120)
left(90)

# Функция отвечает за скорость перемещения черепашки

speed(50)
a = 0
while a < 500:
    forward(150 + a)
    left(90)
    a = a + 20