products = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]

    if action == "Urgent":
       if not item in products:
           products.insert(0, item)

    elif action == "Unnecessary":
        if item in products:
            products.remove(item)

    elif action == "Correct":
        new_item = command[2]
        for index in range(len(products)):
            if products[index] == item:
                products[index] = new_item

    elif action == "Rearrange":
        if item in products:
            products.remove(item)
            products.append(item)

    command = input()

print(", ".join(products))