n = int(input())

capacity = 255
water_in_tank = 0

for number in range (n):
    quantity_water = int(input())
    if capacity < quantity_water:
        print("Insufficient capacity!")
    else:
        capacity -= quantity_water
        water_in_tank += quantity_water
print(water_in_tank)