text = input()

command = input()

while not command.startswith("End"):
    command = command.split()
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]
        while char in text:
            text = text.replace(char, replacement)
        print(text)
    elif action == "Includes":
        string = command[1]
        if string in text:
            result = True
        else:
            result = False
        print(result)
    elif action == "Start":
        string = command[1]
        if text.startswith(string):
            result = True
        else:
            result = False
        print(result)
    elif action == "Lowercase":
        text = text.lower()
        print(text)
    elif action == "FindIndex":
        char = command[1]
        for i in range(len(text) - 1, -1, -1):
            if text[i] == char:
                print(i)
                break
    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)

    command = input()
