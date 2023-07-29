from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "-": subtract,
    "+": add,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What will be the first number?\n"))
    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("What will be the next number?\n"))
        operation_type = operations[operation_symbol]
        answer = operation_type(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}\n")
        user_input = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'e' to exit\n")
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            calculator()
        else:
            should_continue = False

calculator()