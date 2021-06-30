number_of_rooms = int(input())

available_chairs = 0
isEnough = True

for n in range(1, number_of_rooms + 1):
    room = [n for n in input().split()]
    chairs = room[0]
    needed_chairs = int(room[1])

    if len(chairs) >= needed_chairs:
        available_chairs += abs(len(chairs) - needed_chairs)
    else:
        isEnough = False
        print(f"{abs(len(chairs) - needed_chairs)} more chairs needed in room {n}")

if isEnough:
    print(f"Game On, {available_chairs} free chairs left")