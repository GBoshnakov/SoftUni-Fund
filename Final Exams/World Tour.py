text = input()

command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string = command[2]

        if index in range(len(text)):
            text = text[:index] + string + text[index:]
        print(text)

    elif action == "Remove Stop":
        index_start = int(command[1])
        index_end = int(command[2])

        if index_start in range(len(text)) and index_end in range(len(text)):
            text = text[:index_start] + text[index_end + 1:]
        print(text)

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]

        #while old_string in text:
        text = text.replace(old_string, new_string)

        print(text)

    command = input()

print(f"Ready for world tour! Planned stops: {text}")
