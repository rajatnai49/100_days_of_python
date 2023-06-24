from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.start_score()

    def start_score(self):
        self.clear()
        self.read_file()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.start_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.start_score()

    def read_file(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def write_file(self):
        with open("data.txt", mode = "w") as file:
            file.write(f"{self.high_score}")

