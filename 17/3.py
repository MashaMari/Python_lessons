from turtle import *

t = Turtle()
scr = t.getscreen()
scr.onkey(lambda: print('Hello'), 'Up')
scr.listen()
mainloop()