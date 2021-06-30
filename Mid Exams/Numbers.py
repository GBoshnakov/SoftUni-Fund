numbers = [int(n) for n in input().split()]

numbers.sort(reverse=True)

average = sum(numbers) / len(numbers)

result = []

for num in numbers:
    if num > average:
        result.append(num)
        if len(result) == 5:
            break


if not result:
    print("No")
else:
    print(" ".join(list(map(str, result))))