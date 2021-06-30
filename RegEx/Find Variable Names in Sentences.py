import re

text = input()

regex = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"

result = [el.group() for el in re.finditer(regex, text)]


print(*result, sep=",")