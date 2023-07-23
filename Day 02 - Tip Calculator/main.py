# Bill + Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))

tip = int(input("How much percentage yip do you want to give 10, 12 or 15? "))

people = int(input("How many people are you? "))

to_pay = float((bill + ((tip / 100) * bill)) / people)
print(f"$ {round(to_pay, 2)}")
