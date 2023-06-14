from turtle import Turtle
START_POSITION = (0, -280)
MOVE_DIS = 10
FINISH = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(START_POSITION)

    def move_up(self):
        y = self.ycor() + MOVE_DIS
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVE_DIS
        self.goto(self.xcor(), y)

    def start(self):
        self.goto(START_POSITION)
