import turtle

# make the square
s = turtle.Turtle()
for i in range(4):
    s.forward(50)
    s.right(90)
turtle.done()

# make the star
s = turtle.Turtle()
for i in range(5):
    s.forward(50)
    s.right(144)
turtle.done()

# changing line color
s = turtle.Turtle()
s.pencolor("blue")
for i in range(90):
    s.forward(70)
    s.right(55)
s.pencolor("red")
for i in range(90):
    s.forward(90)
    s.right(66)
turtle.done()

# make the circle
s = turtle.Turtle()
s.goto(20,-30)
s.pencolor("red")
s.color("green")
s.speed(100)
for i in range(1,150):
    s.circle(i)
turtle.done()

