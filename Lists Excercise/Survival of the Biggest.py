numbers = input().split()

#numbers_as_int = []

n = int(input())

numbers_as_int = list(map(int, numbers))

# for num in numbers:
#     numbers_as_int.append(int(num))

for num in range(n):
     numbers_as_int.remove(min(numbers_as_int))

print(numbers_as_int)
