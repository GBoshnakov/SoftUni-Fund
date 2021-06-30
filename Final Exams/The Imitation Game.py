text = input()

command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        text = text[number_of_letters:] + text[:number_of_letters]

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        text = text[:index] + value + text[index:]

    elif action == "ChangeAll":
        string_to_find = command[1]
        replacement = command[2]
        while string_to_find in text:
            text = text.replace(string_to_find, replacement)
    command = input()

print(f"The decrypted message is: {text}")