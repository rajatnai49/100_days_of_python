class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 5000,
            "milk": 2000,
            "coffee": 500,
        }
        
    def report(self):
        print("Water: " + str(self.resources['water']) +
            "\nMilk: " + str(self.resources['milk']) +
            "\nCoffee: " + str(self.resources['coffee']))
    
    def is_resource_sufficient(self, drink):
        can_make = True
        for ing in drink.ingrediants:
            if drink.ingrediants[ing] > self.resources[ing]:
                print(f"Sorry there is not enough {ing}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for ing in order.ingrediants:
            self.resources[ing] -= order.ingrediants[ing]
        print(f"Here is your {order.name} 🍵. Enjoy!")

    def add_resources(self, resources):
        for item in self.resources:
            self.resources[item] += resources[item]
        self.report()
