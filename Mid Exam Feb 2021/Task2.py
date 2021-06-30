sugar_cubes = [int(el) for el in input().split()]
command = input()

while not command == "Mort":
    command = command.split()
    action = command[0]
    value = int(command[1])
    if action == "Add":
        sugar_cubes.append(value)
    elif action == "Remove":
        sugar_cubes.remove(value)
    elif action == "Replace":
        repl = int(command[2])
        for i in range(len(sugar_cubes)):
            if sugar_cubes[i] == value:
                sugar_cubes[i] = repl
                break
    elif action == "Collapse":
        sugar_cubes = [sugar_cubes[i] for i in range(len(sugar_cubes))if sugar_cubes[i] >= value]

    command = input()

print(" ".join(list(map(str, sugar_cubes))))
