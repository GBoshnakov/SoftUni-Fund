n = int(input())
searched_word = input()

all_strings = []
filtered_strings = []

for num in range(n):
    string = input()
    all_strings.append(string)

    if searched_word in string:
        filtered_strings.append(string)

print(all_strings)
print(filtered_strings)
