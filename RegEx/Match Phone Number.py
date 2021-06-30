import re

numbers = input()

regex = r"\+359(-| )2\1[0-9]{3}\1[0-9]{4}\b"

result = [el.group() for el in re.finditer(regex, numbers)]

print(*result, sep=", ")