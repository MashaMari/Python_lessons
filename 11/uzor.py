from turtle import *

def draw_tree():
	width(10)
	color('brown')
	fd(50)
	left(90)
	fd(50)
	left(180)
	color('green', 'green')
	begin_fill()
	for i in range(3):
		fd(100)
		left(120)
	end_fill()
	up()
	fd(50)
	right(90)
	fd(50)
	right(180)
	
#draw_tree()

speed(50)

for i in range(8):
	up()
	fd(100)
	down()
	draw_tree()
	up()
	bk(100)
	down()
	left(360/8)

color('white')	


#	up()
#	fd(150)
#	down()
#	for i in range(4):
#		fd(100)
#		left(90)
#	up()
#	bk(150)
#end_fill()

input()
