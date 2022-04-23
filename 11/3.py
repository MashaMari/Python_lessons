from turtle import *

color('blue')
# forward(99)
# left(120)
# forward(33)
# left(120)
# forward(33)
# right(120)
# forward(33)
# left(120)
# forward(33)
# right(120)
# forward(33)
# left(120)
# forward(33)
# input()


def draw_triangle(length):
    left(60)
    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)
    left(180)
    forward(length)

def draw_n_triangles(n_triangle, length):
    for i in range(n_triangle):
        draw_triangle(length)


draw_n_triangles(3, 100)
# draw_triangle(100)
input()