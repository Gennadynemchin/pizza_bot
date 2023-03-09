import json


with open("addresses.json", "r") as addresses:
    addresses = addresses.read()

with open("menu.json", "r") as menu:
    menu_pizza = menu.read()

addresses = json.loads(addresses)
menu = json.loads(menu_pizza)
print(addresses)
print(menu_pizza)
