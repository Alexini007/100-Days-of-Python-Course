print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to treasure island")
print("YOu shall find the treasure!")

choice1 = input('You\'re at a crossroad, do you want to go left or right? Type "left or "right"\n').lower()

if choice1 == "right":
    choice2 = input("You have to cross the river, but you don't have much time. Do you wait for a boat or swim? Type 'swim' or 'wait'\n").lower()
    if choice2 == "swim":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors - yellow, red and green. Which one do you choose?\n").lower()
        if choice3 == "green":
            print("You found the tresure! You win!")
        else:
            print("Unfortunately, you didn't find the fortune")
    else:
        print("Your enemies caught up with you because you waited for too long. Game over!")
else:
    print("The path ended. Game over!")