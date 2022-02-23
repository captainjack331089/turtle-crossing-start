import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.create_car()
    car.move_cars()

    #detect player collision with the car
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect player if hit the top of the wall
    if player.ycor() >= 300:
        player.origin()
        car.level_up()
        scoreboard.level_up()
        scoreboard.update()

screen.exitonclick()
