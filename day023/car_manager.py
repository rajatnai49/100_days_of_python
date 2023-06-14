from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING = 5
MOVE_ICR = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.speed = STARTING
        self.icr = MOVE_ICR

    def add_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def increment_speed(self):
        self.speed += self.icr

    def car_move(self):
        for car in self.cars:
            car.backward(self.speed)
