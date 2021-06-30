starting_deck = input().split()

n = int(input())


half = int((len(starting_deck) / 2))


for num in range(n):
    left_half = starting_deck[0:half]
    right_half = starting_deck[half:]
    current_deck = []
    for index in range(len(left_half)):
        current_deck.append(left_half[index])
        current_deck.append((right_half[index]))

    starting_deck = current_deck
print(starting_deck)

