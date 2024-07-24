#Ripple Patel
#Portfolio Project using Turtle API

import turtle
import math

turtle.shape("turtle")
# turtle.speed(0)
# turtle.color("blue")
# turtle.pensize(5)


size = 100
def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def house(len):
    square(len)
    triangle(len)

def octagon(len):
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)

def stop_sign(len):
    octagon(len)
    turtle.penup()
    turtle.forward(3/8 * len)
    turtle.pendown()
    turtle.forward(len / 5)  # Width of the sign post
    turtle.right(90)
    turtle.forward(len * 2)  # Height of the sign post
    turtle.right(90)
    turtle.forward(len / 5)
    turtle.right(90)
    turtle.forward(len * 2)
    turtle.right(90)





def main():
    turtle.speed(20)
    turtle.color("blue")
    turtle.pensize(5)
    house(100)
    turtle.color("red")
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    house(50)

def rect(x,y):
    for i in range(2):
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(90)

#turtle.forward(100)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)

# square(100)
# turtle.penup()
# turtle.forward(125)
# turtle.pendown()
# square(100)

# main()

# rect(50,170)
# turtle.penup()
# turtle.forward(125)
# turtle.pendown()
#square(200)

# octagon(100)
# turtle.forward(25)
# rect(50,170)

stop_sign(70)
turtle.penup()
turtle.forward(150)
turtle.pendown()
stop_sign(50)

# turtle.hideturtle()
# turtle.done()
turtle.Screen().exitonclick()