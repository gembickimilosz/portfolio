import turtle
import math

def jump(length):
    """Move forward without drawing."""
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

def rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def rhombus(side_length, angle):
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(angle)
        turtle.forward(side_length)
        turtle.left(180 - angle)

def parallelogram(side1, side2, angle):
    for _ in range(2):
        turtle.forward(side1)
        turtle.left(angle)
        turtle.forward(side2)
        turtle.left(180 - angle)

def rectangle_from_parallelogram(width, height):
    parallelogram(width, height, 90)

def rhombus_from_parallelogram(side_length, angle):
    parallelogram(side_length, side_length, angle)

def triangle(length, angle):
    turtle.forward(length)
    turtle.left(180 - angle)
    turtle.forward(length)
    turtle.left(angle)

def draw_pie(n, length):
    angle = 360 / n
    for _ in range(n):
        triangle(length, angle)
        turtle.left(angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    steps = int(arc_length / 3) + 1
    step_length = arc_length / steps
    step_angle = angle / steps

    for _ in range(steps):
        turtle.forward(step_length)
        turtle.left(step_angle)

def petal(radius, angle):
    for _ in range(2):
        arc(radius, angle)
        turtle.left(180 - angle)

def flower(n, radius, angle):
    for _ in range(n):
        petal(radius, angle)
        turtle.left(360 / n)

def spiral(turns, step=5, angle=20):
    distance = step
    for _ in range(turns):
        turtle.forward(distance)
        turtle.left(angle)
        distance += step

def setup():
    turtle.reset()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.color("purple")

if __name__ == "__main__":
    setup()

    rectangle(80, 40)
    # rhombus(50, 60)
    # rectangle_from_parallelogram(80, 40)
    # rhombus_from_parallelogram(50, 60)
    # draw_pie(6, 50)
    # flower(7, 60, 60)
    # spiral(50, step=5, angle=20)

    turtle.done()
