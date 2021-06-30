data = input()
command = input()

while not command == "Done":
    command = command.split()
    action = command[0]

    if action == 'Change':
        char = command[1]
        replacement = command[2]
        data = data.replace(char, replacement)
        print(data)
    elif action == 'Includes':
        string = command[1]
        if string in data:
            print(True)
        else:
            print(False)
    elif action == 'End':
        string = command[1]
        if data.endswith(string):
            print(True)
        else:
            print(False)
    elif action == 'Uppercase':
        data = data.upper()
        print(data)
    elif action == 'FindIndex':
        char = command[1]
        for i in range(len(data)):
            if data[i] == char:
                print(i)
                break
    elif action == 'Cut':
        start_index = int(command[1])
        length = int(command[2])
        data = data[start_index:start_index+length]
        print(data)

    command = input()