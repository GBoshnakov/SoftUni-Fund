import re

text = input()

regex = r"(^|(?<=\s))-?\d+(\.?\d+)?($|(?=\s))"

result = [el.group() for el in re.finditer(regex, text)]

print(*result)