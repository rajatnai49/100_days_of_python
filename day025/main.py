import turtle
import pandas 

FONT = ("Courier", 16, "normal")

screen = turtle.Screen()
screen.title("INDIAN STATES GAME")
image = "india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

name = "hello".title()
x, y = int(100), int(100)
t.goto(x, y)
t.write(f"{name}", font=FONT)

turtle.mainloop()
