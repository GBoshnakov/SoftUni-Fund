import re
text = input()
regex = r"(@|#)[a-zA-Z]{3,}\1\1[a-zA-Z]{3,}\1"

mirrors = []

matches = [el.group() for el in re.finditer(regex, text)]

for el in matches:
    half = len(el) // 2
    left_part = el[:half]
    right_part = el[half:]
    if left_part == right_part[::-1]:
        mirrors.append(left_part.strip("@#") + " <=> " + right_part.strip("@#"))

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirrors:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(*mirrors, sep=", ")

