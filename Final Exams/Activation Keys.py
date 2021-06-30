key = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if case == "Upper":
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
            print(key)
        elif case == "Lower":
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
            print(key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[:start_index] + key[end_index:]
        print(key)
    command = input()

print(f"Your activation key is: {key}")
