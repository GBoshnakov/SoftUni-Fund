import re
text = input()
points = 0

regex = r"(?<=(=|/))[A-Z][A-Za-z]{2,}(?=(\1))"

result = [el.group() for el in re.finditer(regex, text)]

print(f"Destinations: {', '.join(result)}")
for el in result:
    points += len(el)
print(f"Travel Points: {points}")