import re

text = input()

cool_ones = []

regex = r"(::|\*\*)[A-Z][a-z]{2,}(\1)"

target_threshold = 1
for char in text:
    if char.isdigit():
        target_threshold *= int(char)

emojis = [el.group() for el in re.finditer(regex, text)]

for emoji in emojis:
    coolness = 0
    for n in emoji:
        if n.isalpha():
            coolness += ord(n)
    if coolness > target_threshold:
        cool_ones.append(emoji.strip())

print(f"Cool threshold: {target_threshold}")

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
if cool_ones:
    print(*cool_ones, sep="\n")