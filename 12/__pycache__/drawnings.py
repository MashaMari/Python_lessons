from turtle import *
from math import sin, radians, tan


def roof(angle, length):
	forward(length)
	left((180+angle)// 2)
	forward((length/2)/sin(radians(angle / 2)))
	left(180-angle)
	forward((length/2)/sin(radians(angle / 2)))
	left((180+angle)// 2)


def poly(num):
	angle = 360 / num
	for i in range(num):
		forward(100)
		left(angle)

def house():
	color("red")
	begin_fill()
	roof(120, 100)
	end_fill()
	color("orange")
	begin_fill()
	right(90)
	poly(4)
	end_fill()

def window():
	color('blue')
	begin_fill()
	for i in range(4):
		fd(40)
		right(90)
	end_fill()	

def pine():
	color("brown")
	down()
	begin_fill()
	for i in range(2):
		fd(50)
		left(90)
		fd(20)
		left(90)
	end_fill()	
	# Ствол дерева

	goto(-210, -130)
	color("green")
	left(90)
	begin_fill()
	roof(30, 100)
	roof(30, 100)
	end_fill()
	right(90)
	up()

def sun():
	color("yellow")
	begin_fill()
	circle(30)
	end_fill()
	left(90)
	fd(30)	

	for i in range(10):
		up()
		right(36)
		#print(i*36)
		if i % 2 == 0:
			l = 10
		else:
			l = 15
		fd(30 + 10)
		fd(tan(radians(75))*(l//2))
		right(90)
		fd(5)
		left(180)
		down()

		begin_fill()
		roof(30, l)
		up()
		end_fill()

		fd(5)
		left(90)
		fd(30 + 10)
		fd(tan(radians(75))*(l//2))
		left(180)


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


def cloud():
	speed(0)
	color("white")
	begin_fill()
	circle(20, steps=100)
	end_fill()

	#up()
	fd(60)
	left(90)
	fd(30)
	begin_fill()
	circle(30, steps=100)
	end_fill()
	right(90)

	fd(20)
	left(90)
	begin_fill()
	circle(25, steps=100)
	end_fill()
	right(90)


	fd(15)
	left(90)
	back(10)
	begin_fill()
	circle(20, steps=100)
	end_fill()
	right(90)

# house()
# window()
# roof(60)
# pine()
# speed(100)
# sun()
# cloud()
# input()