import turtle as t
import random
import numpy as np

color_list = np.random.randint(0, 256, size=(26, 3))
colors = [tuple(rgb) for rgb in color_list]

t.Turtle()

random_color = (random.choice(colors))
t.colormode(255)
t.penup()
t.speed("fastest")
t.hideturtle()


def left_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(0)


def right_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(100)


for _ in range(5):
    for _ in range(10):
        t.dot(20, (random.choice(colors)))
        t.setheading(180)
        t.forward(50)
    left_up()
    for _ in range(10):
        t.forward(50)
        t.dot(20, (random.choice(colors)))
    right_up()

screen = t.Screen()
screen.exitonclick()
