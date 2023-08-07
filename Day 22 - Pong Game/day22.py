from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong Game")
my_screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(r_paddle.paddle_up, "Up")
my_screen.onkey(r_paddle.paddle_down, "Down")
my_screen.onkey(l_paddle.paddle_up, "w")
my_screen.onkey(l_paddle.paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect Right paddle misses
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset()

    # Detect Left paddle misses
    if ball.xcor() <-380:
        scoreboard.right_point()
        ball.reset()

    if scoreboard.r_score >= 10 or scoreboard.l_score >= 10:
        game_is_on = False
        scoreboard.end_of_game()
my_screen.exitonclick()