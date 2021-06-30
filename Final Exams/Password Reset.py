text = input()



command = input()

while command != "Done":
    new_text = ""
    if command == "TakeOdd":
        for i in range(1, len(text), 2):
            new_text += text[i]
        print(new_text)
        text = new_text

    else:
        command = command.split()
        action = command[0]

        if action == "Cut":
            index = int(command[1])
            lenght = int(command[2])
            searched_word = text[index:index + lenght]
            text = text.replace(searched_word, "", 1)
            print(text)

        elif action == "Substitute":
            searched_element = command[1]
            element = command[2]
            if searched_element in text:
                while searched_element in text:
                    text = text.replace(searched_element, element)
                print(text)
            else:
                print("Nothing to replace!")
    command = input()

print(f"Your password is: {text}")