n = int(input())

sum = 0
for num in range(1, n + 1):
    num1 = str(num)
    for number in num1:

        sum += int(number)
    if sum == 5 or sum == 7 or sum == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

    sum = 0