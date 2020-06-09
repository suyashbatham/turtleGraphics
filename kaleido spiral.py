import turtle
import time as p
from itertools import cycle

t = turtle.Turtle()

colors = cycle(['red','blue','green','yellow','orange','grey','purple','pink','black'])
def circle(angle,size,forw,shape):
    t.pencolor(next(colors))
    next_shape = ""
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size*2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+5,next_shape)

t.speed('fast')
t.pensize(4)
circle(30,0,1,'circle')

t.fillcolor('green')

p.sleep(2)
t.hideturtle()

turtle.done()