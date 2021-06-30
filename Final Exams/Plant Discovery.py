import statistics
n = int(input())

plants = {}

for num in range(n):
    item, rarity = input().split("<->")
    rarity = int(rarity)

    if item not in plants:
        plants[item] = {"rarity": 0, "rating": []}
    plants[item]["rarity"] = rarity

command = input()

while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    string = command[1]

    if action == "Rate":
        plant, rating = string.split(" - ")
        rating = int(rating)
        if plant in plants:
            plants[plant]["rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant, new_rarity = string.split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        if string in plants:
            plants[string]["rating"] = []
        else:
            print("error")
    else:
        print("error")

    command = input()

for key, val in plants.items():
    if val['rating']:
        plants[key]["average_rating"] = statistics.mean(val['rating'])
    else:
        plants[key]["average_rating"] = 0
sorted_plants = sorted(plants.items(),key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['average_rating']))

print("Plants for the exhibition:")
for key, val in sorted_plants:
    print(f"- {key}; Rarity: {val['rarity']}; Rating: {val['average_rating']:.2f}")