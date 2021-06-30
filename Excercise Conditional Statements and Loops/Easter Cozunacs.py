budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price

cozunacs_counter = 0
colored_eggs = 0
price_per_cozunac = flour_price + eggs_price + (milk_price / 4)

while budget >= price_per_cozunac:
    budget -= flour_price + eggs_price + (milk_price / 4)
    cozunacs_counter += 1
    colored_eggs += 3
    if cozunacs_counter % 3 == 0:
        colored_eggs -= cozunacs_counter - 2

print(f'You made {cozunacs_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')


