elements = input().split()

counter = 0

command = input()

while command != "end":
    index_1, index_2 = [int(n) for n in command.split()]
    counter += 1

    if index_1 == index_2 or index_1 not in range(len(elements)) or index_2 not in range(len(elements)):
        elements.insert(len(elements) // 2, "-" + str(counter) + "a"), elements.insert(len(elements) // 2, "-" + str(counter) + "a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[index_1] != elements[index_2]:
        print("Try again!")
    elif elements[index_1] == elements[index_2]:
        print(f"Congrats! You have found matching elements - {elements[index_1]}!")
        elements = [elements[n] for n in range(len(elements)) if n != index_1 and n != index_2]

    if not elements:
        print(f"You have won in {counter} turns!")
        break
    command = input()

if elements:
    print(f"Sorry you lose :(")
    print(" ".join(elements))
