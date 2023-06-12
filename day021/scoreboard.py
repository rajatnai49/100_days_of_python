from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    def start_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.start_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
