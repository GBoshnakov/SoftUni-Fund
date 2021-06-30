command = input()

force_book = {}

while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        side = command[0]
        user = command[1]
        if side not in force_book:
            force_book[side] = []
        if user not in force_book[side]:
            force_book[side].append(user)

    elif '>' in command:
        side_user = command.split(' -> ')
        side = side_user[1]
        user = side_user[0]
        for force, users in force_book.items():
            if user in users:
                users.remove(user)
                break
        if side not in force_book:
            force_book[side] = [user]
            print(f"{user} joins the {side} side!")
        elif side in force_book and user not in force_book[side]:
            force_book[side].append(user)
            print(f"{user} joins the {side} side!")

    command = input()

filtered_book = sorted(force_book.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]))

for key, val in filtered_book:
    if len(val) > 0:
        print(f"Side: {key}, Members: {len(val)}")
        for el in sorted(val):
            print(f"! {el}")