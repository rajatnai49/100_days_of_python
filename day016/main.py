from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem(name="latte", cost=2.5, milk=150, water=200, coffee=24),
espresso = MenuItem(name="espresso", cost=1.5, milk=0, water=50, coffee=18),
cappuccino = MenuItem(name="cappuccino", cost=3, milk=50, water=250, coffee=24),

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    choice = input(f"What would you like? Choose between espresso, latte or cappuccino: ")
    if choice == "off":
        print("Have a good one!")
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee_choice) and money_machine.make_payment(coffee_choice.cost):
            coffee_maker.make_coffee(coffee_choice)