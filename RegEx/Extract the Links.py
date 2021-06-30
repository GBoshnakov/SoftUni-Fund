import re

text = input()

links = []

regex = r"www.[a-zA-Z0-9\-]+(\.[a-zA-Z]+)+"
while text:

    result = [el.group() for el in re.finditer(regex, text)]
    links.extend(result)

    text = input()

print(*links, sep="\n")

