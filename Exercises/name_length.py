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
