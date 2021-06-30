neighbourhood = [int(n) for n in input().split("@")]

isSuccessful = True
counter = 0

command = input()

starting_index = 0

while command != "Love!":
    command = command.split()

    current_index = int(command[1])

    if starting_index + current_index <= len(neighbourhood) - 1:

        starting_index += current_index
        if neighbourhood[starting_index] <= 0:
            print(f"Place {starting_index} already had Valentine's day.")
        else:
            neighbourhood[starting_index] -= 2
            if neighbourhood[starting_index] <= 0:
                print(f"Place {starting_index} has Valentine's day.")

    else:
        starting_index = 0
        if neighbourhood[starting_index] <= 0:
            print(f"Place {starting_index} already had Valentine's day.")
        else:
            neighbourhood[starting_index] -= 2
            if neighbourhood[starting_index] <= 0:
                print(f"Place {starting_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {starting_index}.")

for el in neighbourhood:
    if el != 0:
        isSuccessful = False
        counter += 1

if isSuccessful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
