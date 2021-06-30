data = input().split()

legendary_items = {"shards": 0, "fragments": 0, "motes": 0}

materials_to_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

junk_items = {}

is_obtainted = False

while not is_obtainted:

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        item = data[i + 1].lower()
        if item in legendary_items:
            legendary_items[item] += quantity
        else:
            if item not in junk_items:
                junk_items[item] = 0
            junk_items[item] += quantity

        for key, val in legendary_items.items():
            if val >= 250:
                legendary_items[key] -= 250
                print(f"{materials_to_items[key]} obtained!")
                is_obtainted = True
                break

        if is_obtainted:
            break
    if is_obtainted:
        break
    data = input().split()

sorted_items = sorted(legendary_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, val in sorted_items:
    print(f"{key}: {val}")

junk_items = sorted(junk_items.items(), key=lambda kvp: kvp[0])
for key, val in junk_items:
    print(f"{key}: {val}")