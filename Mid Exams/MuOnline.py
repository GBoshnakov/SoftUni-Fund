import sys
string = input().split("|")

bitcoins = 0

health = 100

for i in range(len(string)):
    event = string[i].split()
    command = event[0]
    value = int(event[1])

    if command == "potion":
        temp_health = health
        health += value
        if health > 100:
            health = 100

        print(f"You healed for {health - temp_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value

        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            sys.exit()

        print(f"You slayed {command}.")
print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")

