number = int(input())

music = {}

for n in range(number):
    piece, composer, key = input().split("|")
    music[piece] = {'composer': composer, 'key': key }

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":

        composer = command[2]
        key = command[3]
        if piece in music:
            print(f"{piece} is already in the collection!")
        else:
            music[piece] = {'composer': composer, 'key': key }
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece in music:
            del music[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in music:
            music[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_music = sorted(music.items(), key=lambda kvp: (kvp[0], kvp[1]['composer']))



for key, val in sorted_music:
    print(f"{key} -> Composer: {val['composer']}, Key: {val['key']}")