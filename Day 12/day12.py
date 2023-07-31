import random
from art import logo

def generate_number():
    num = random.randint(1, 100)
    return num


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    number = generate_number()
    lives = 0
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    for i in range(lives, 0, -1):
        print(f"You have {lives} attempts remaining to guess the number. ")
        lives -= 1
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Guess is too high")
        elif guess < number:
            print("Guess is too low")
        elif guess == number:
            print(f"You got it the answer was {number}")
            break

    if input("Do you want to play another game?\n") == "y":
        game()

game()

