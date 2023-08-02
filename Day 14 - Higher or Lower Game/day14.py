import random
from data import data
import art


def pick_person():
    num = random.randint(0, len(data) - 1)
    return data[num]


def format_data(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"


def game():
    print(art.logo)
    score = 0
    choice1 = pick_person()
    choice2 = pick_person()
    should_continue = True

    while should_continue:
        choice1 = choice2
        choice2 = pick_person()
        while choice1 == choice2:
            choice2 = pick_person()

        print(f"Compare A: {format_data(choice1)}.")
        print(art.vs)
        print(f"Against B: {format_data(choice2)}.")
        user_answer = input("Who has more followers? Type 'A or 'B':\n")

        if (user_answer == 'A' or user_answer == 'a') and choice1['follower_count'] > choice2['follower_count']:
            score += 1
            print(f"You are right! Current score {score}\n")
        elif (user_answer == 'A' or user_answer == 'a') and choice1['follower_count'] < choice2['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False
        elif (user_answer == 'B' or user_answer == 'b') and choice1['follower_count'] > choice2['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False
        elif (user_answer == 'B' or user_answer == 'b') and choice1['follower_count'] < choice2['follower_count']:
            score += 1
            print(f"You are right! Current score {score}\n")


game()


