item_ratings = [int(n) for n in input().split()]

entry_point = int(input())

type_item = input()

left_side = item_ratings[:entry_point]
right_side = item_ratings[entry_point + 1:]
left_side_damage = 0
right_side_damage = 0

if type_item == "cheap":
    for el in left_side:
        if el < item_ratings[entry_point]:
            left_side_damage += el

    for el_2 in right_side:
        if el_2 < item_ratings[entry_point]:
            right_side_damage += el_2

elif type_item == "expensive":
    for el in left_side:
        if el >= item_ratings[entry_point]:
            left_side_damage += el

    for el_2 in right_side:
        if el_2 >= item_ratings[entry_point]:
            right_side_damage += el_2

if left_side_damage >= right_side_damage:
    print(f"Left - {left_side_damage}")
else:
    print(f"Right - {right_side_damage}")