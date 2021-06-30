word = input()
list1 = []

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        list1.append(i)

print(list1)