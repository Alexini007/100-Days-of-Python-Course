from turtle import Turtle, Screen
import random
is_race_on = False

my_sreen = Screen()
my_sreen.setup(width=500, height=400)
user_bet = my_sreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_position = 90
for n in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[n])
    new_turtle.goto(x=-230, y=y_position)
    y_position -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


my_sreen.exitonclick()