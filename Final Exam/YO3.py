command = input()

users = {}

while command != "Log out":
    command = command.split(": ")
    action = command[0]
    username = command[1]

    if action == "New follower":
        if username not in users:
            users[username] = {"likes":0, "comments": 0, "total": 0}
    elif action == "Like":
        count = int(command[2])
        if username not in users:
            users[username] = {"likes":0, "comments": 0, "total": 0}
        users[username]["likes"] += count
        users[username]["total"] += count
    elif action == "Comment":
        if username not in users:
            users[username] = {"likes":0, "comments": 0, "total": 0}
        users[username]["comments"] += 1
        users[username]["total"] += 1
    elif action == "Blocked":
        if username in users:
            del users[username]
        else:
            print(f"{username} doesn't exist.")

    command = input()

sorted_users = sorted(users.items(), key= lambda kvp: (-kvp[1]["total"], kvp[0]))

print(f"{len(users)} followers")
for key, val in sorted_users:
    print(f"{key}: {val['total']}")
