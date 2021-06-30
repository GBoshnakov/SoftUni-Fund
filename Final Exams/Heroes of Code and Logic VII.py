n = int(input())

heroes = {}

for num in range(n):
    data = input().split()
    hero = data[0]
    hp = int(data[1])
    mp = int(data[2])

    heroes[hero] = {"hp": hp, "mp": mp}

command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes[hero]["mp"] >= mp_needed:
            heroes[hero]["mp"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes[hero]["hp"] -= damage
        if heroes[hero]["hp"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]

    elif action == "Recharge":
        hero = command[1]
        amount = int(command[2])

        if heroes[hero]["mp"] + amount > 200:

            print(f"{hero} recharged for {200 - heroes[hero]['mp']} MP!")
            heroes[hero]["mp"] = 200
        else:
            heroes[hero]["mp"] += amount
            print(f"{hero} recharged for {amount} MP!")

    elif action == "Heal":
        hero = command[1]
        amount = int(command[2])

        if heroes[hero]["hp"] + amount > 100:

            print(f"{hero} healed for {100 - heroes[hero]['hp']} HP!")
            heroes[hero]["hp"] = 100
        else:
            heroes[hero]["hp"] += amount
            print(f"{hero} healed for {amount} HP!")

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp:(-kvp[1]["hp"], kvp[0]))

for key, val in sorted_heroes:
    print(key)
    print(f"  HP: {val['hp']}")
    print(f"  MP: {val['mp']}")