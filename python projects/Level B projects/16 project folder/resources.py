
#* Solution starts on line 100

































































































# class supplies:
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "milk": milk,
#             "coffee": coffee
#         }


# class Inventory:
#     def __init__(self):
#         self.menu = [
#             supplies(name="latte", water=200, milk=150, coffee=24, cost=2.5),
#             supplies(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
#             supplies(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
#         ]

#     def items(self):
#         options = ""
#         for item in self.menu:
#             options += f"{item.name}/"
#         return options

#     def find_drink(self, order_name):
#         for item in self.menu:
#             if item.name == order_name:
#                 return item
#         print("That it is unavailable.")