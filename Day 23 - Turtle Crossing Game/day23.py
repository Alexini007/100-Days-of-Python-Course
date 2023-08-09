import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import FINISH_LINE_Y

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
player = Player()
car_manager = CarManager()
my_screen.listen()
my_screen.onkey(player.player_move, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game()
    if player.ycor() > FINISH_LINE_Y:
        player.set_position()
        car_manager.increase_speed()
        scoreboard.level_up()

my_screen.exitonclick()