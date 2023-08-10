import pandas
import turtle

my_screen = turtle.Screen()
my_screen.title("US States Game")
my_screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")


states_file = pandas.read_csv("50_states.csv")
states_list = states_file["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = my_screen.textinput(title=f"{len(guessed_states)}/50 Guessed States", prompt="Name another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_file[states_file.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)


# Create a csv file with all the states the user did not manage to guess
not_guessed_states = []
for state in states_list:
    if state not in guessed_states:
        not_guessed_states.append(state)

new_data = pandas.DataFrame(not_guessed_states)
new_data.to_csv("not_guessed_states.csv")


