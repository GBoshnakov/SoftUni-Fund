total_order = 0
taxes = 0
part_price = input()


while part_price != "special" and part_price != "regular":
    part_price = float(part_price)

    if part_price < 0:
        print("Invalid price!")
    else:
        total_order += part_price

    part_price = input()

if total_order == 0:
    print("Invalid order!")
else:
    taxes = 0.2 * total_order
    total_order += taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_order - taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if part_price == "special":
        total_order = 0.9 * total_order
    print(f"Total price: {total_order:.2f}$")