# # Print the length of a string
# print(6 + 2.0)
# print(len(input("What is your name?")))
# # --------------------------------------
#
# # Store the input inside a variable
# name = input("What is your name?")
# print(name)
# # ---------------------------------------
#
# # Reverse a & b's values
# a = input("a: ")
# b = input("b: ")
#
# temp = a
# a = b
# b = temp
#
# print("a: " + a)
# print("b: " + b)
#
# # ---------------------------------------
#
# # Adds digits of a number
# two_digit_number = input("Type a two digit number: ")
# digit1 = str(two_digit_number[0])
# digit2 = str(two_digit_number[1])
# print(int(digit1) + int(digit2))
#
# # ---------------------------------------
# # Calculate BMI
#
# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# BMI = weight / (height ** 2)
# print(int(BMI))
#
# # ---------------------------------------
# # Check if its odd or even number
# number = int(input("Which number do you want to check? "))
# if number % 2 == 1:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")
#
# # ---------------------------------------
# # Calculate BMI 2.0
#
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = round(weight / (height ** 2))
#
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")
#
# # ---------------------------------------
# # Check if a given year is a leap year
#
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0 and year % 100 != 0:
#     print("Leap year.")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not leap year.")
#
# # ---------------------------------------
# # Pizza ordering
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# total = 0
#
# if size == "S":
#     total += 15
#     if add_pepperoni == "Y":
#         total += 2
# elif size == "M":
#     total += 20
#     if add_pepperoni == "Y":
#         total += 3
# elif size == "L":
#     total += 25
#     if add_pepperoni == "Y":
#         total += 3
# else:
#     print("Invalid pizza size, please pick from S, M or L")
#     size = input("What size pizza do you want? S, M, or L ")
#
# if extra_cheese == "Y":
#     total += 1
# print(f"Your final bill is: ${total}.")
#
# # ---------------------------------------
# # lower() and count()
# name1 = name.lower()
# times = name1.count("e")

# # ---------------------------------------
# # Random numbers
#
# import random
#
# random_num = random.randint(10, 100)
# print(random_num)
# random_num = random.random()
# print(random_num)

# # ---------------------------------------
# # Lists
#
# states = ["Mississippi", "Texas", "Montana", "Ohio"]
# print(states[3])
# states.append("New York")
# print(states)

# # ---------------------------------------
# # Random entry from a list
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma.")
# names = names_string.split(", ")
# num_of_people = len(names)
# random_num = random.randint(0, num_of_people - 1)
# print(f"{names[random_num]} is going to buy the meal today!")

# # ---------------------------------------
# # Map a spot X on the Tic-Tac-Toe
#
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# my_map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = str(input("Where do you want to put the treasure? "))
# my_map[int(position[1]) - 1][int(position[0]) - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

# # ---------------------------------------
# # Loops
#
# fruits = ["apple", "peach", "banana"]
# for fruit in fruits:
#     print(fruit)

# # ---------------------------------------
# # Input a list with loop, and then calculate average height
#
# student_heights = input ("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# count = 0
# total = 0
# for height in student_heights:
#     total += height
#     count += 1
# print(round(total / count))

# # ---------------------------------------
# # Determine highest score with a loop
#
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max = student_scores[0]
# for num in student_scores:
#     if num > max:
#         max = num
#
# print(f"The highest score in the class is: {max}")

# # ---------------------------------------
# # Calculate the sum of all the even numbers from 1 to 100
#
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
#
# # or
#
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# ---------------------------------------
# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
