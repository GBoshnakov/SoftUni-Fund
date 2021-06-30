treasure = input().split("|")
stolen_items = []
lenght_sum = 0

command = input()

while command != "Yohoho!":
    command = command.split()

    if command[0] == "Loot":
        command = [command[i] for i in range(1, len(command)) if command[i] not in treasure]
        for i in range(len(command)):
            treasure.insert(0, command[i])

    elif command[0] == "Drop":
        index = int(command[1])
        if index in range(len(treasure)):
            treasure.append(treasure[int(command[1])])
            treasure.pop(int(command[1]))

    elif command[0] == "Steal":
        stolen_items = []
        count = int(command[1])
        if count > len(treasure):
            stolen_items = treasure
            treasure = []
            print(", ".join(stolen_items))
        else:
            stolen_items += treasure[len(treasure) - count:]
            treasure = treasure[:len(treasure) - count]
            print(", ".join(stolen_items))

    command = input()

if not treasure:
    print("Failed treasure hunt.")
else:
    for n in treasure:
        lenght_sum += len(n)
    print(f"Average treasure gain: {lenght_sum / len(treasure):.2f} pirate credits.")

