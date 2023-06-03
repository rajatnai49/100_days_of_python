class MenuItem:
    def __init__(self, name, cost, milk, water, coffee):
        self.name = name
        self.cost = cost
        self.ingrediants = {
            "milk": milk,
            "water": water,
            "coffee": coffee,
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost=2.5, milk=150, water=200, coffee=24),
            MenuItem(name="espresso", cost=1.5, milk=0, water=50, coffee=18),
            MenuItem(name="cappuccino", cost=3, milk=50, water=250, coffee=24),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item