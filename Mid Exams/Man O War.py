pirate_ship = [int(n) for n in input().split(">")]
war_ship = [int(n) for n in input().split(">")]

max_health = int(input())

command = input()

while command != "Retire":
    command = command.split()
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(war_ship)):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)

    elif action == "Defend":
        index_start = int(command[1])
        index_end = int(command[2])
        damage = int(command[3])

        if index_start in range(len(pirate_ship)) and index_end in range(len(pirate_ship)):
            for i in range(index_start, index_end + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship)):
            if pirate_ship[index] < max_health:
                pirate_ship[index] += health
                if pirate_ship[index] > max_health:
                    pirate_ship[index] = max_health

    elif action == "Status":
        counter_of_sections = 0
        for el in pirate_ship:
            if el < max_health * 0.2:
                counter_of_sections += 1
        print(f'{counter_of_sections} sections need repair.')

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ship)}")