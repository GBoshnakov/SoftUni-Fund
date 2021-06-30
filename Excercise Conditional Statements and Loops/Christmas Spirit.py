quantity = int(input())
days_left = int(input())

spirit = 0
cost = 0
current_day = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

while days_left > 0:
    current_day += 1
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        cost += ornament_set * quantity
        spirit += 5
    if current_day % 3 == 0:
        cost += tree_skirt * quantity
        cost += tree_garland * quantity
        spirit += 13
    if current_day % 5 == 0:
        cost += tree_lights * quantity
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        cost += tree_skirt + tree_garland + tree_lights
        spirit -= 20



    days_left -= 1


if current_day % 10 == 0:
    spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')