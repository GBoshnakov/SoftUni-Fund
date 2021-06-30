command = input()

items_price = {}
items_quantity = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in items_price:
        items_price[name] = 0
        items_quantity[name] = 0
    items_price[name] = price
    items_quantity[name] += quantity

    command = input()

for key, val in items_price.items():
    total_price = items_price[key] * items_quantity[key]
    print(f"{key} -> {total_price:.2f}")