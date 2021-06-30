import sys
action_list = input().split("|")

energy = 100
coins = 100


for n in action_list:
    current_list = n.split("-")
    event = current_list[0]
    amount = int(current_list[1])
    current_energy = energy

    if event == "rest":

        if energy + amount >= 100:

            print(f"You gained {current_energy - 100} energy.")
            energy = 100
        else:
            energy += amount
            print(f"You gained {amount} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy - 30 >= 0:
            coins += amount
            energy -= 30
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        coins -= amount
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            sys.exit(0)
print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")