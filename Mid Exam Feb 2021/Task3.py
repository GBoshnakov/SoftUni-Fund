price = [int(el) for el in input().split()]
entry_point = int(input())
item = input()

left_side_damage = price[:entry_point]
right_side_damage = price[entry_point+1:]

left_damage = 0
right_damage = 0

if item == "cheap":
    for i in left_side_damage:
        if i < price[entry_point]:
            left_damage += i

    for y in right_side_damage:
        if y < price[entry_point]:
            right_damage += y

elif item == "expensive":
    for i in left_side_damage:
        if i >= price[entry_point]:
            left_damage += i

    for y in right_side_damage:
        if y >= price[entry_point]:
            right_damage += y

if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")
