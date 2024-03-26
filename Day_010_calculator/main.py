#Calculator
from art import logo
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    calculating = True

    num1 = float(input("What is the first number?: "))
    for op in operations:
        print(op)

    while calculating:
        operator = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculation = operations[operator]
        answer = calculation(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if(input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")).lower() == 'y':
            num1 = answer
        else:
            calculating = False
            calculator()

calculator()