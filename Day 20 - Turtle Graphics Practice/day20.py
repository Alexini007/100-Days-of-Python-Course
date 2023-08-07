from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.setup(width=600, height = 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        segments[seg_num].goto(segments[seg_num - 1].xcor(), segments[seg_num - 1].ycor())
    segments[0].forward(20)


my_screen.exitonclick()



