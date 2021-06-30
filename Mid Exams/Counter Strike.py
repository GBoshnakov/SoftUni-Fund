energy = int(input())
distance = input()

wins = 0

while distance != "End of battle":
    distance = int(distance)
    if distance <= energy:
        energy -= distance
        wins += 1

        if wins % 3 == 0:
            energy += wins

    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break


    distance = input()

if distance == "End of battle":
    print(f"Won battles: {wins}. Energy left: {energy}")
