import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_manager.numbers < 50:
        car_manager.add_car()
    car_manager.update_car(scoreboard.level)

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("Game over! You lose!")
            game_is_on = False
            scoreboard.game_over()

    if player.reach_finish():
        print("Next level!")
        scoreboard.update_score()
        player.reset_pos()

screen.exitonclick()
