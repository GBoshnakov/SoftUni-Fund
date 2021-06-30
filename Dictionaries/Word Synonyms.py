n = int(input())

synonyms = {}

for n in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = synonym
    else:
        synonyms[word] += f", {synonym}"

for word in synonyms:
    print(f"{word} - {synonyms[word]}")