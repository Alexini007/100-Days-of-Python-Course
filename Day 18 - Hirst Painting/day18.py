import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colours = [(207, 160, 160), (54, 88, 88), (145, 91, 91), (140, 26, 26), (221, 207, 207), (132, 177, 177), (158, 46, 46),
 (45, 55, 55), (169, 160, 160), (129, 189, 189), (83, 20, 20), (37, 43, 43), (186, 94, 94), (187, 140, 140),
 (85, 120, 120), (59, 39, 39)]

steve = Turtle()
steve.penup()
steve.speed("fastest")
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    steve.dot(20, random.choice(colours))
    steve.forward(50)
    if dot_count % 10 == 0:
        steve.left(90)
        steve.forward(50)
        steve.left(90)
        steve.forward(50*10)
        steve.setheading(0)
steve.hideturtle()

my_screen = Screen()

my_screen.exitonclick()
