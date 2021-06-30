products = input().split("|")

budget = int(input())
profit = 0
new_list = []


for i in range(len(products)):

    current_product = products[i].split("->")
    product = current_product[0]
    price = float(current_product[1])

    if product == "Clothes" and price <= 50 and budget - price >= 0:
       budget -= price
       new_price = round((price * 1.4), 2)
       profit += new_price - price
       new_list.append(new_price)


    elif product == "Shoes" and price <= 35 and budget - price >= 0:
        budget -= price
        new_price = round((price * 1.4), 2)
        profit += new_price - price
        new_list.append(new_price)


    elif product == "Accessories" and price <= 20.50 and budget - price >= 0:
        budget -= price
        new_price = round((price * 1.4), 2)
        profit += new_price - price
        new_list.append(new_price)

for num in new_list:
    print(f'{num:.2f}', end=" ")
print()


print(f"Profit: {profit:.2f}")

if sum(new_list) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")






