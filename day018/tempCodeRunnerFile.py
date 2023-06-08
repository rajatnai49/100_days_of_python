
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
