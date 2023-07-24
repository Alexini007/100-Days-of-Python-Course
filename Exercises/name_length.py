# Print the length of a string
print(6 + 2.0)
print(len(input("What is your name?")))
# --------------------------------------

# Store the input inside a variable
name = input("What is your name?")
print(name)
# ---------------------------------------

# Reverse a & b's values
a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

# ---------------------------------------

# Adds digits of a number
two_digit_number = input("Type a two digit number: ")
digit1 = str(two_digit_number[0])
digit2 = str(two_digit_number[1])
print(int(digit1)+int(digit2))

# ---------------------------------------
# Calculate BMI

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
BMI = weight/(height ** 2)
print(int(BMI))

# ---------------------------------------
# Check if its odd or even number
number = int(input("Which number do you want to check? "))
if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

# ---------------------------------------
# Calculate BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight/(height ** 2))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

# ---------------------------------------
# Check if a given year is a leap year

year = int(input("Which year do you want to check? "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year.")

# ---------------------------------------
# Pizza ordering

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total = 0

if size == "S":
    total += 15
    if add_pepperoni == "Y":
        total += 2
elif size == "M":
    total += 20
    if add_pepperoni == "Y":
        total += 3
elif size == "L":
    total += 25
    if add_pepperoni == "Y":
        total += 3
else:
    print("Invalid pizza size, please pick from S, M or L")
    size = input("What size pizza do you want? S, M, or L ")

if extra_cheese == "Y":
    total += 1
print(f"Your final bill is: ${total}.")

# ---------------------------------------
# lower() and count()
name1 = name.lower()
times = name1.count("e")