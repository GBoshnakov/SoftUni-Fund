gift_ideas = input().split()

result = ""

command_string = input()



while not command_string == "No Money":
    command_list = command_string.split()
    command = command_list[0]
    gift = command_list[1]

    if command == "OutOfStock":

        for i in range(len(gift_ideas)):
            if gift_ideas[i] == gift:
                gift_ideas[i] = "None"
    elif command == "Required":
        index = int(command_list[2])

        if len(gift_ideas) - 1 >= index >= 0:
            gift_ideas[index] = gift
    elif command == "JustInCase":
        gift_ideas[-1] = gift
    command_string = input()

for n in gift_ideas:
    if n != "None":
        print(f'{n}', end=" ")




