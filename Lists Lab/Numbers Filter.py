n = int(input())

evens = []
odds = []
positives = []
negatives = []


for num in range(n):
    number = int(input())

    if number % 2 == 0:
        evens.append(number)

    if number % 2 == 1:
        odds.append(number)

    if number < 0:
        negatives.append(number)

    if number >= 0:
        positives.append(number)

command = input()

if command == "even":
    print(evens)
elif command == "odds":
    print(odds)
elif command == "positive":
    print(positives)
elif command == "negative":
    print(negatives)


