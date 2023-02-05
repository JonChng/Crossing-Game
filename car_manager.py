from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_list = []

    def create_car(self):
        random_chance = random.randint(1,6)

        if random_chance == 1:

            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))

            y_cor = random.randint(-250, 301)
            x_cor = 300
            car.goto(x_cor, y_cor)
            self.car_list.append(car)


    def travel(self):
        for i in self.car_list:
            i.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT







