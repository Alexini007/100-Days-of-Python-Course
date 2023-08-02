import menu

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= menu.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + nickles + dimes + pennies
    return total


def is_transaction_ok(money_received, cost):
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += cost
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded: $ {round(money_received, 2)}")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        break
    if user_input == "report":
        print(f"Water: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")
        print(f"Coffee: {menu.resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = menu.MENU[user_input]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_ok(payment, drink['cost']):
                make_coffee(user_input, drink['ingredients'])
