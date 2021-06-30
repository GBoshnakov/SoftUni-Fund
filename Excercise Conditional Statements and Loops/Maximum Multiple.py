divisor = int(input())
bound = int(input())
import sys

max = 0

for number in range(1,bound + 1):
    if number % divisor == 0 and number <= bound and number > 0:
        max = number
        if max < sys.maxsize:
            continue

print(max)



