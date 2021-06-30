words = input()

total_sum = 0

word_1, word_2 = words.split()

if len(word_1) == len(word_2):
    for i in range(len(word_1)):
        total_sum += ord(word_1[i]) * ord(word_2[i])
elif len(word_1) > len(word_2):
    for i in range(len(word_2)):
        total_sum += ord(word_1[i]) * ord(word_2[i])
    for i in range(len(word_2), len(word_1)):
        total_sum += ord(word_1[i])
else:
    for i in range(len(word_1)):
        total_sum += ord(word_1[i]) * ord(word_2[i])
    for i in range(len(word_1), len(word_2)):
        total_sum += ord(word_2[i])
print(total_sum)