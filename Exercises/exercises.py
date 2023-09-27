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


# ---------------------------------------
# Inheritance example

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__() # inherit all attributes and methods of animal
#
#     def breathe(self):
#         super().breathe()   # using breathe method from animal
#         print("but underwater")
#     def swim(self):
#         print("Swimming")
#
# nemo = Fish()
# nemo.swim()
# nemo.num_eyes
# nemo.breathe()


# ---------------------------------------
# Slicing lists and tuples

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[2:5])   # prints c d e
# print(letters[2:])    # prints all onwards from c to the end
# print(letters[:5])    # prints all before e
# print(letters[2:5:2]) # print c e, third number is increment
# print(letters[::-1])  # REVERSING LIST

# ---------------------------------------
# Accessing a file on the desktop with an absolute path
# with open(r"C:/Users/asus/Desktop/data.txt") as file:


# ---------------------------------------
# Pandas DateFrame and Series

# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["temp"])

# # Convert data frame to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Converts series to a list

# temp_list = data["temp"].to_list()

# # Get data from a column

# print(data["condition"])
# print(data.condition)

# # Get data from a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 9/5 + 32)

# # Create a data frame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
#
# # Send that data to a csv file
# data.to_csv("new_data.csv")

# # Get column Primary Fur Color and turn it to list

# data_list = data["Primary Fur Color"].to_list()
# print(data_list)

# # Get rows where the value in column Primary Fur is Gray and then get the count of these rows

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel count")


# ---------------------------------------
# List Comprehension

# nums = [1, 2, 3]
# new_list = [n+1 for n in nums]
# print(new_list)
#
# # List that doubles the numbers in the given range
# new_list2 = [n*2 for n in range(1,5)]
# print(new_list2)
#
# # Create new list with just the short names from the first list
# names = ["Danny", "Jill", "Dave", "Eleanor", "Steve", "Beth", "Elizabeth"]
# new_names = [name for name in names if len(name) <= 4]
# print(new_names)
# new_names2 = [name.upper() for name in names if len(name) > 5]
# print(new_names2)
#
# # Take only even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# Compare numbers in 2 files and print out the matching ones
# with open("file1.txt") as data1:
#     file1_nums = data1.readlines()
#
# with open("file2.txt") as data2:
#     file2_nums = data2.readlines()
#
# result = [int(n) for n in file1_nums if n in file2_nums]
# print(result)

# ---------------------------------------
# Dictionary Comprehension
# import random
# names = ["Danny", "Jill", "Dave", "Eleanor", "Steve", "Beth", "Elizabeth"]
# students_scores = {name: random.randint(1, 100) for name in names}
#
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)

# Converting a sentence to a list. Then counting the number of letters in the words
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split(" ")
# result = {word: len(word) for word in word_list }
# print(result)
#
# # We have a dictionary with a day and temperature. Make a new dictionary with converted temperature
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f ={day: (temp * 9/5) + 32 for(day, temp) in weather_c.items()}
# print(weather_f)

# ---------------------------------------
# How to iterate over a dictionary; and a Pandas DataFrame

# student_dict = {
#     "student": ["Angela", "James", "Lilly"],
#     "score": [56, 76, 98]
# }
# for (key, value) in student_dict.items():
#     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #print(row.student)
#     #print(row.score)
#     if row.student == "Angela":
#         print(row.score)

# ---------------------------------------
# Tkinter library

# from tkinter import *
# #
# my_window = Tk()
# my_window.title("First GUI Project")
# my_window.minsize(width=500, height=300)
# my_window.config(padx=20, pady=20)
# # # Label
# #
# my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# #my_label.pack(side="left")  # pack label on the screen
# my_label["text"] = "New text"  # change the text of label
# my_label.config(text="New text")  # change the text of label
# my_label.grid(column=0, row=0)  # use a grid
# #
# # # Button
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text=input_n.get())
#
# button = Button(text="Click me", command=button_clicked)
# #button.place(x=0, y=20)   # TOP LEFT CORNER IS (0, 0)
# button.grid(column=1, row=1)  # use a grid
#
#
# # # Input - Entry
# input_n = Entry(width=10)
# input_n.get()
# input_n.grid(column=3, row=2)  # use a grid
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# # Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
#
# my_window.mainloop()  # has to be on the bottom to keep the window showing

# function can take as many inputs as you want/Unlimited arguments/Many positional arguments
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     print(total)
#
#
# add(5, 6, 3)
#
#
# # Optional keyword arguments
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#
#
# calculate(2, add=3, multiply=5)
#
#
# # Creating a class with **kwargs
# class Car:
#     def __init__(self, **kwargs):
#         self.model = kwargs["model"]  # this will give error if we don't put it in argument
#         self.year = kwargs.get("model")  # if this does not exist it won't give error - it will be None
#
#
# my_car = Car(year=2004, model="Skyline")
#
#
# # kwargs are put into a dictionary
# # args are put in a list
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)  # Output will be 4 (7, 3, 0) {'x': 10, 'y': 64}

# ---------------------------------------
# FileNot found exception; KeyError exception

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict)
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write('Sth')
#     print("File error")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

# ---------------------------------------
# Create own exception

# height = float(input("Height:"))
# weight = int(input("Weight"))
#
# if height > 3:
#     raise ValueError("Your height can't be over 3 meters")
# bmi = weight / (height ** 2)
# print(bmi)

# ---------------------------------------
# Catch IndexError - index out of bounds

# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

# ---------------------------------------
# Send email with smtplib

# import smtplib
# my_email = "**"
# password = "****"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="**", msg="Subject: Test\n\nlets test")


# ---------------------------------------
# Datetime library

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year= 1995, month= 12, day=15, hour=4)
# print(date_of_birth)


# ---------------------------------------
# Send email with text from file

# import smtplib
# import datetime as dt
# import random
#
# my_email = "**"
# password = "****"
#
# now = dt.datetime.now()
# if now.weekday() == 2:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         chosen_quote = random.choice(all_quotes)
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=my_email,
#                             msg=f"Subject: Motivational Quote\n\n{chosen_quote}")


# ---------------------------------------
# Making API Calls

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)   # -> Response 200
# response.raise_for_status()
# # HTTP Status Codes:
# # 1xx = informational response
# # 2xx = everything was successful
# # 3xx = redirection
# # 4xx = doesn't exist or problem is within you, not authorized
# # 5xx = server fault (down or issue)
#
# data = response.json()  # actual json data
# print(data)
# print(data["iss_position"]["latitude"])


# ---------------------------------------
# Specifying data type - Data Type Hint

# age: int
# name: str
#
#
# def police_check(person_age: int) -> bool:  # function expecting parameter of type int and to return boolean type
#     if person_age > 18:
#         return "Can drive"


# ---------------------------------------
# Web Scraping with Beautiful Soup

# from bs4 import BeautifulSoup

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.p)
# print(soup.title.string)
# all_tags = soup.find_all(name="a")
#
# for tag in all_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# heading2 = soup.find(name="h3", class_="heading")
# print(heading2.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)

# ---------------------------------------
# Web Scraping with Beautiful Soup

# import requests
#
# response = requests.get("https://news.ycombinator.com")
# yc_webpage = response.text
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# article_texts = []
# article_links = []
#
# title_line = soup.select(".titleline")
#
# for line in title_line:
#     text = line.find("a").text
#     article_texts.append(text)
#     link = line.find("a").get("href")
#     article_links.append(link)
#
# article_upvotes = [int(score.text.split()[0]) for score in soup.select(".score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)

# ---------------------------------------
# Web Scraping with Selenium

# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
# print(article_count.text)

# ---------------------------------------
# Selenium write inputs and click buttons

# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# input1 = driver.find_element(By.NAME, value="fName")
# input1.send_keys("First")
#
# input2 = driver.find_element(By.NAME, value="lName")
# input2.send_keys("Last")
#
# input3 = driver.find_element(By.NAME, value="email")
# input3.send_keys("test@gmail.com")
# submit = driver.find_element(By.CSS_SELECTOR, value="form button")
# submit.click()

# ---------------------------------------
# Selenium scraping Amazon webpage (additional code to pass Captcha)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
#
# # ua = UserAgent()
# # user_agent = ua.random
# #
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# #
# # options.add_argument(f'--user-agent={user_agent}')
# #
# driver = webdriver.Chrome(options=options)
# #
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# #
# # price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# # price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# #
# # print(price_dollar, price_cents)

# ---------------------------------------
# Command Line cheat sheet(commands)

# pwd - print working directory
# cd - change directory
# mkdir - make directory
# touch - create a file
# ls - list
# rm - remove a file
# rm -rf folder_name - delete folders

# ---------------------------------------
# Creating Python Decorator
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function()
#
#
# @delay_decorator
# def say_hello():
#     print("Hi!")


# ---------------------------------------
# How to import and run Flask

# from flask import Flask
# app = Flask(__name__)
#
# # makes sure that this hello_world function is only triggered if the user access this URL(home_page/)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/bye")
# def bye():
#     return "<p>Bye, Bye!</p>"
#
# if __name__ == "__main__":
#     app.run()


# ---------------------------------------
# How to take parameter of URL and use it FLASK

# @app.route("/username/<name>/<int:number>")
# def hello(name, number):
#     return f"Hello, {name} , your ID: {number}!"

# ---------------------------------------
# Use decorator to make functions bold

# def make_bold(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper
#
# @app.route('/bye')
# @make_bold
# def bye():
#     return 'Bye'

# ---------------------------------------
# Use decorator with args and kwargs

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged = False
#
#
# def authentication_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged == True:
#             function(args[0])
#     return wrapper
#
# @authentication_decorator
# def create_post(name):
#     print(f"This is {name}'s post")
#
# new_user = User("Gogi")
# new_user.is_logged = True
# create_post(new_user)

# ---------------------------------------
# Use decorator with args and kwargs

# def logging_decorator(function):
#     def wrapper(*args):
#         print(f"You called {function.__name__}{args}")
#         result = function(*args)
#         print(f"It returned: {result}")
#     return wrapper
#
#
# # Use the decorator 👇
#
# @logging_decorator
# def a_function(*args):
#     product = 1
#     for arg in args:
#         product *= arg
#     return product
#
# a_function(2, 2, 3)

# ---------------------------------------
# Check for prime number

# def check_prime(num):
#     is_prime = True
#     for i in range(2, num - 1):
#         if num % i == 0:
#             print("Not Prime")
#             is_prime = False
#             break
#     if is_prime == True:
#         print("Prime")


# ---------------------------------------
# Sum of number's digits

# sum = 0
# digit_1 = number // 100
# digit_2 = (number % 100) // 10
# digit_3 = number % 10
# sum = digit_3 + digit_2 + digit_1
# print(sum)

# ---------------------------------------
# Sum of number's digits


# string = input("Str")
# new_string = ''
# for char in string:
#     if 'A' <= char <= 'Z':
#         new_string += chr(ord(char) + 32)
#     else:
#         new_string += char


# ---------------------------------------
# Format numbers

# print(new_string)
# num = 15.7345345
# print(f"The num is {num:>20.2f}")
# print("The num is {:<20.2f}".format(num))
# print(f"The num is {1+2:>10}")
# print(f"The num is {17.6767:^6.2f}")


# name = "Alex"
# id = "34567890"
# print(f"My name is: {name:>20}")
# print("My name is: {:>20}".format(name))
# print(f"My id is: {id:>22}")
# print("My id is: {:>22}".format(id))