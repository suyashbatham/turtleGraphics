# link : https://docs.python.org/2/library/turtle.html

import turtle as t

# 1.goto
# t.goto(100,200)

# 2.penup , pendown
t.penup()   # emove the cursor line
t.goto(200,300)
t.pendown()
t.goto(200,300)   # make the line
t.color('blue')
t.pensize(20)
t.goto(20,333)
t.speed(50) # increase the speed
t.getscreen().bgcolor('blue')
t.forward(300)
t.left(90)
t.right(30)
t.done()