import turtle

obj = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("Black")
obj.color("White")
obj.speed(0)

for i in range (120):
    obj.circle(i+8)
    obj.left(30)

for a in range (60):
    obj.circle(a+4)
    obj.right(30)

turtle.done()