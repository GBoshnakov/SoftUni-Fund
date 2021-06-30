import re

text = input()

regex = r"(^|(?<=\s))[a-zA-Z0-9]+[\.\_\-]?[a-z0-9]+?@[a-z]+-?[a-z]+(\.[a-z]+)+"

result = [el.group() for el in re.finditer(regex, text)]

for el in result:
    print(el)