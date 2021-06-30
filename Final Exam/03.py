command = input()

guests = {}
unliked_meals = []

while command != "Stop":
    action, guest, meal = command.split("-")
    if action == "Like":
        if guest not in guests:
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif action == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        else:
            if meal not in guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                guests[guest].remove(meal)
                unliked_meals.append(meal)
    command = input()

sorted_guests = sorted(guests.items(), key=lambda kvp:(-len(kvp[1]), kvp[0]))

for key, val in sorted_guests:
    print(f"{key}: {', '.join(val)}")
print(f"Unliked meals: {len(unliked_meals)}")