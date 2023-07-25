import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice not in [0, 1, 2]:
    user_choice = int(input("Invalid input, choose again? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

comp_choice = random.randint(0, 2)
options = [rock, paper, scissors]
print("You:")
print(options[user_choice])
print("Computer:")
print(options[comp_choice])

if user_choice == 0 and comp_choice == 2:
    print("You win")
elif user_choice == 2 and comp_choice == 0:
    print("Computer wins")
elif user_choice > comp_choice:
    print("You win")
elif user_choice == comp_choice:
    print("Draw")
else:
    print("Computer wins")

