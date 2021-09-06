from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSSIBLE_POSITIONS = list(range(-220, 220, 25))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.numbers = 0

    def car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        color = random.choice(COLORS)
        car.color(color)
        car.setheading(180)
        car.goto(300, random.choice(POSSIBLE_POSITIONS))
        self.all_cars.append(car)

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cars_added = random.randint(0, 3)
            position_to_add = random.sample(POSSIBLE_POSITIONS, k=cars_added)
            for pos in position_to_add:
                self.car()
            self.numbers += cars_added

    def update_car(self, level):
        for car in self.all_cars:
            if car.xcor() > -350:
                car.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT * 0.1)
            else:
                self.all_cars.remove(car)
                self.numbers -= 1
                del car
                print("Deleted!")
