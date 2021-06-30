targets = [int(n) for n in input().split()]

command = input()

while command != "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        if len(targets) > index >= 0:
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if len(targets) > index + value and index - value >= 0:
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    command = input()

targets = [str(n) for n in targets]

print(f'{"|".join(targets)}')