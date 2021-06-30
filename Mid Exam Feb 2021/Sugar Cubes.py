sugars = [int(n) for n in input().split()]

command = input()

while command != "Mort":
    command = command.split()
    action = command[0]
    value = int(command[1])

    if action == "Add":
        sugars.append(value)
    elif action == "Remove":
        sugars.remove(value)
    elif action == "Replace":
        replacement = int(command[2])
        for i in range(len(sugars)):
            if sugars[i] == value:
                sugars[i] = replacement
                break
    elif action == "Collapse":
        sugars = [sugars[i] for i in range(len(sugars)) if sugars[i] >= value]

    command = input()

print(" ".join(list(map(str, sugars))))