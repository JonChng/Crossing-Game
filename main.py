import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

turtle = Player()
cars = CarManager()
board = Scoreboard()

screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.travel()

    for i in cars.car_list:
        car_x = i.xcor()
        low_x = car_x - 20
        high_x = car_x + 20

        if turtle.distance(i) < 28 and (turtle.xcor() >= low_x and turtle.xcor() <= high_x):
            game_is_on = False
            board.clear()
            board.end()

    if turtle.check():
        cars.level_up()
        turtle.reset()
        board.clear()
        board.next_level()
    screen.update()




screen.exitonclick()