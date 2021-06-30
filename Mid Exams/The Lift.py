people_waiting = int(input())

wagons = [int(n) for n in input().split()]

for i in range(len(wagons)):
    difference = 4 - wagons[i]
    if difference <= people_waiting:
        people_waiting -= difference
        wagons[i] += difference
    else:
        wagons[i] += people_waiting
        people_waiting = 0

if people_waiting > 0 and wagons.count(4) == len(wagons):
    print(f"There isn't enough space! {people_waiting} people in a queue!")

elif people_waiting == 0 and wagons.count(4) < len(wagons):
    print("The lift has empty spots!")

print(" ".join(list(map(str, wagons))))