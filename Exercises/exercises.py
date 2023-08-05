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

# # ---------------------------------------
# # FizzBuzz
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# # ---------------------------------------
# # Calling functions
#
# def greet(name, location):
#     print(f"Hello {name}")
#     print(f"How's the weather in {location}")
#
#
# greet("Alex", "Plovdiv")
# greet(location="Sofia", name="Gosho")

# # ---------------------------------------
# # Calculates area to be painted
#
# import math
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
#
# def paint_calc(height, width, cover):
#     num_of_cans = (height * width) / cover
#     num_of_cans = math.ceil(num_of_cans)
#     print(f"You'll need {num_of_cans} cans of paint.")
#
#
# paint_calc(test_h, test_w, coverage)

# # ---------------------------------------
# # Checks if number is prime or not
#
# def prime_checker(number):
#     if number % 2 == 0 or number % 3 == 0:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")
#
# n = int(input("Check this number: "))
# prime_checker(number = n)

# or

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

# # ---------------------------------------
# # Dictionaries
#
#
#
# print(dict["normal"])
# print(dict["name"])
#
# dict["nickname"] = "num"  # add to dictionary
# print(dict)
# dict["normal"] = 6  # edit entry from dictionary
# print(dict)
#
# for key in dict:
#     print(key)  # will print only the keys -> normal, name and nickname
#     print(dict[key])  # will print only values

# # ---------------------------------------
# # Students grade dictionary
#
#
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
#
# student_grades = {}
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)

# # ---------------------------------------
# # Nested dictionaries & lists
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": "Berlin"
# }
#
# travel_log1 = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": "Berlin"
# }
#
# travel_log1 = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12
#      },
#     {"country": "Germany",
#      "cities_visited": ["Dortmund", "Hamburg"],
#      "total_visits": 17
#      }
# ]

# # ---------------------------------------
# # Add to dictionary
#
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# def add_new_country(country, times, cities):
#     new_country = {"country": country, "visits": times, "cities": cities}
#     travel_log.append(new_country)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# dictionary = {"a": 1, "b": 2, "c": 3, 1: 4, 2: 5}
#
# print(dictionary[2])

# # ---------------------------------------
# # Returning functions
# def my_func():
#     result = 2 * 3
#     return result
#
#
# print(my_func())


# # ---------------------------------------
# # Function that determines days of a month
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True and month == 2:
#         return 29
#     return month_days[month - 1]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# ---------------------------------------
# Already imported classes Turtle, Screen and library prettytable from pypi

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("aquamarine")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
#
# table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

# ---------------------------------------
# Creating class with constructor
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person1 = User("Goshko", 18)
# print(f"{person1.name} is {person1.age} years old")

# ---------------------------------------
# Drawing dashed line with Turtle class

# from turtle import Turtle, Screen
#
# steve_the_turtle = Turtle()
# steve_the_turtle.shape("turtle")
# steve_the_turtle.color("green")
#
# for n in range(6):
#     steve_the_turtle.pendown()
#     steve_the_turtle.forward(10)
#     steve_the_turtle.penup()
#     steve_the_turtle.forward(10)
#
#
# screen = Screen()
# screen.exitonclick()

# ---------------------------------------
# Drawing a shapes with specific number of sides

# from turtle import Turtle, Screen
# import random
# steve_the_turtle = Turtle()
# steve_the_turtle.shape("turtle")
# steve_the_turtle.color("green")
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen" ]
#
# def draw_figure(num_sides):
#     for n in range(num_sides):
#         angle = 360 / num_sides
#         steve_the_turtle.forward(100)
#         steve_the_turtle.right(angle)
#
# for shape_side_n in range(3, 11):
#     steve_the_turtle.color(random.choice(colours))
#     draw_figure(shape_side_n)
# screen = Screen()
# screen.exitonclick()

# ---------------------------------------
# Drawing a Random Walk

# steve_the_turtle.pensize(10)
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen" ]
# directions = [0, 90, 180, 270]
#
# for n in range(50):
#     steve_the_turtle.color(random.choice(colours))
#     steve_the_turtle.forward(30)
#     steve_the_turtle.setheading(random.choice(directions))

# ---------------------------------------
# Drawing a Spirograph - multiple circles

# for n in range(36):
#     steve_the_turtle.circle(50)
#     steve_the_turtle.right(10)

