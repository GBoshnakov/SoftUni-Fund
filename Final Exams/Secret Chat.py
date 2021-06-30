message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        while substring in message:
            message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
