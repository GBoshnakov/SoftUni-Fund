companions = int(input())
days = int(input())

earnings = 0

for day in range (1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    earnings += 50 - (companions * 2)
    if day % 3 == 0:
        earnings -= companions * 3
    if day % 5 == 0:
        earnings += companions * 20
        if day % 3 == 0:
            earnings -= companions * 2

print(f'{companions} companions received {int(earnings / companions)} coins each.')
