items = input().split(", ")

command = input().split(" - ")

while "Craft!" not in command:
    command_one = command[0]
    command_two = command[1]

    if command_one == "Collect":
        if command_two not in items:
            items.append(command_two)
    elif command_one == "Drop":
        if command_two in items:
            items.remove(command_two)
    elif command_one == "Combine Items":
        command_list = command_two.split(":")
        old_item = command_list[0]
        new_item = command_list[1]
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif command_one == "Renew":
        if command_two in items:
            items.remove(command_two)
            items.append(command_two)


    command = input().split(" - ")

print(", ".join(items))
