import turtle
import pandas
from turtle import *

FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("INDIAN STATES GAME")
image = "india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("28_states.csv")
state_list = data.state.to_list()
guessed = []

while len(guessed) < 28:
    answer = screen.textinput(
        title=f"{len(guessed)}/28 States Guessed", prompt="Name a State").title()

    if answer == "Exit":
        missing = []
        for state in state_list:
            if state not in guessed:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in state_list:
        if answer not in guessed:
            guessed.append(answer)
            check_ans = data[data.state == answer]
            x, y = int(check_ans.x), int(check_ans.y)
            t.goto(x, y)
            t.write(f"{answer}")

# Code for getting position on the turtle canvas
# def print_position(x, y):
#     print("Mouse Position:", x, y)
# screen.onclick(print_position)

turtle.mainloop()
