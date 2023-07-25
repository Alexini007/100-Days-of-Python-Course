# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))

password_characters = []
for n in range(1, num_of_letters + 1):
    password_characters.append(random.choice(letters))

for n in range(1, num_of_numbers + 1):
    password_characters.append(random.choice(numbers))

for n in range(1, num_of_symbols + 1):
    password_characters.append(random.choice(symbols))

random.shuffle(password_characters)
password = ""
for char in password_characters:
    password += char

print("Your password is " + password)
