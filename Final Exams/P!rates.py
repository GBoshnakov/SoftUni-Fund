cities = {}

data = input()

while data != "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold

    data = input()

command = input()

while command != "End":
    command = command.split("=>")
    action = command[0]

    if action == "Plunder":
        city = command[1]
        people = int(command[2])
        gold = int(command[3])

        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            print(f"{city} has been wiped off the map!")
            del cities[city]

    elif action == "Prosper":
        city = command[1]
        gold = int(command[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

    command = input()

sorted_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, val in sorted_cities:
        print(f"{key} -> Population: {val['population']} citizens, Gold: {val['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
