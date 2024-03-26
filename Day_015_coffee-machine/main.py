## Coffee machine
# Menu items and their requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

low_resources = {
    "water": 100,
    "milk": 100,
    "coffee": 25,
}

units_of_mesurement = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

powered_on = True

#Coin operated; coin values
penny_value = 0.01
dime_value = 0.10
nickel_value = 0.05
quarter_value = 0.25

#print a report to tell how much resourcese are left
def report():
    """Show the remaining resources"""
    for i in resources:
        print(f"{i.title()}: {resources[i]}{units_of_mesurement[i]}")

#Alternate text values that underline the first character of choices
water = "\033[4mw\033[0mater"
milk = "\033[4mm\033[0milk"
coffee = "\033[4mc\033[0moffee"
exit = "\033[4me\033[0mxit"
#Refill resources
def refill():
    """Funtion to refill resources"""
    report()
    choice = input(f"Which would you like to refill: ({water}/{milk}/{coffee}/{exit}): ").lower()
    if (choice == "water") or (choice == "milk") or (choice == "coffe") or (choice == "exit") or (choice == "w") or (choice == "m") or (choice == "c") or (choice == "e"):
        if choice == "w":
            choice = "water"
        if choice == "m":
            choice = "milk"
        if choice == "c":
            choice = "coffee"
        if choice != "exit" or choice != "e":
            amount = int(input("How much would you like to refill: "))
            resources[choice] += amount
    else:
        print("Unsupported request")

#Shutdown the machine
def power_off():
    """returns false and to be used with powered_on bool"""
    print("Good bye.")
    return False

#check if the resources match the requirment for the requested drinkk
def check_resources(requested_drink):
    """check the resources before processing order"""
    drink = MENU[requested_drink]
    for i in drink["ingredients"]:
        if resources[i] < drink["ingredients"][i]:
            print(f"Not enough mineral. Please refill {i}")

    print(f"{requested_drink} cost: ${drink['cost']:.2f}")
    payment = take_payment()
    if payment < drink["cost"]:
        print(f"Insufficient funds: ${payment:.2f}. Returning money")
    else:
        make_drink(requested_drink)
        change = payment - drink["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {requested_drink}. Enjoy!")


#make the requested drink
def make_drink(requested_drink):
    """make ghe drink and deduct the amount of resources"""
    drink = MENU[requested_drink]
    for i in drink["ingredients"]:
        resources[i] -= drink["ingredients"][i]

    #Check if the reasources are low after making the last drink and notify the user
    for i in resources:
        if resources[i] <= low_resources[i]:
            print(f"Low {i}. Please refill {i}")

def take_payment():
    """Take the users payment"""
    print("please insert coins")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    payment = (quarter * quarter_value) + (dimes * dime_value) + (nickles * nickel_value) + (pennies * penny_value)

    return payment

#Alternate text values that underline the first character of choices
espresso = "\033[4me\033[0mspresso"
latte = "\033[4ml\033[0matte"
cappuccino = "\033[4mc\033[0mappuccino"
#Loop to continue operations
while powered_on:
    request = input(f"What would you like? ({espresso}/{latte}/{cappuccino}): ").lower()

    if (request == "report"):
        report()
    elif (request == "refill"):
        refill()
    elif (request == "power off") or (request == "shut down"):
        powered_on = power_off()
    elif (request == "espresso") or (request == "latte") or (request == "cappuccino") or (request == "e") or (request == "l") or (request == "c"):
        if request == "e":
            request = "espresso"
        if request == "l":
            request = "latte"
        if request == "c":
            request = "cappuccino"
        check_resources(request)
    else:
        print("Unsupported request")

    print("\n")
