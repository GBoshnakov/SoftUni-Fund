cards = input()


list_of_cards = cards.split()
list_of_cards = set(list_of_cards)

is_Over = False

team_A = 11
team_B = 11

for element in list_of_cards:
    if "A" in element:
        team_A -= 1
        if team_A == 6:
            is_Over = True
            break
    elif "B" in element:
        team_B -= 1
        if team_B == 6:
            is_Over = True
            break

print(f'Team A - {team_A}; Team B - {team_B}')
if is_Over:
    print("Game was terminated")



