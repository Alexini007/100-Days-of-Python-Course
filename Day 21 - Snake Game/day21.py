from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.reposition_food()
        snake.enlarge_snake()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        # creating game border
        scoreboard.reset()
        snake.reset()
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

my_screen.exitonclick()