products = input()

product_stock = {}

while products != "statistics":
    products = products.split(": ")
    product = products[0]
    quantity = int(products[1])

    if product in product_stock:
        product_stock[product] += quantity
    else:
        product_stock[product] = quantity

    products = input()

print("Products in stock:")

for key, value in product_stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(product_stock)}")
print(f"Total Quantity: {sum(product_stock.values())}")