n = int(input())

sum_of_chars = 0

for num in range(n):
    char = input()

    sum_of_chars += ord(char)

print(f'The sum equals: {sum_of_chars}')