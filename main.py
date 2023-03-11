import json


with open("jsons/addresses.json", "r") as addresses:
    addresses = addresses.read()

with open("jsons/menu.json", "r") as menu:
    menu_pizza = menu.read()

addresses = json.loads(addresses)
menu = json.loads(menu_pizza)


for element in menu:
    name = element['name']
    slug = 123
    sku = 456
    description = element['description']

    print(name, slug, sku, description)
