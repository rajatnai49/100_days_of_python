import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.car_move()

    if player.ycor() > 310:
        score.player_point()
        player.start()
        car_manager.increment_speed()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
