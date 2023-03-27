menu = {
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
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}

money = {
    "value": 0,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")

def check_resources(choice):
    enough = True
    if menu[choice]['ingredients']['water'] > resources['water']:
        print(f"There isn't enough water for a {choice}.")
        enough = False
    if menu[choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There isn't enough coffee for a {choice}.")
        enough = False
    if choice != 'espresso' and menu[choice]['ingredients']['milk'] > resources['milk']:
        print(f"There isn't enough milk for a {choice}.")
        enough = False
    return enough

def deduct_resources(choice):
    resources['water'] -= menu[choice]['ingredients']['water']
    resources['coffee'] -= menu[choice]['ingredients']['coffee']
    if choice != '  espresso':
        resources['milk'] -= menu[choice]['ingredients']['milk']

def process_coins(given, choice):
    needed = menu[choice]["cost"]
    total = 0
    total += given['quarters']*0.25
    total += given['dimes']*0.10
    total += given['nickles']*0.05
    total += given['pennies']*0.01
    if total < needed:
        print(f"Not enough money, refunded!")
        return False
    else:
        deduct_resources(choice)
        money["value"] += needed
        change = round(total-needed, 2)
        if change != 0.00:
            print(f"Here your change ${change}")
        return True


def coffee_machine():
    on = True
    while on:
        choice = input(
            "What would you like? 'espresso', 'latte', 'cappuccino': ")
        if choice == "report":
            report()
            coffee_machine()
        elif choice == "off":
            print("Turning off")
            on = False
        elif check_resources(choice):
            print(f"Please insert coins. Total should be ${menu[choice]['cost']}")
            given = {}
            given['quarters'] = int(input("How many quarters?: "))
            given['dimes'] = int(input("How many dimes?: "))
            given['nickles'] = int(input("How many nickles?: "))
            given['pennies'] = int(input("How many pennies?: "))
            if process_coins(given, choice):
                print(f"Here is your {choice} !!")
            
coffee_machine()