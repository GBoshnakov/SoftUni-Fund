import re

text = input()

regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = re.findall(regex, text)

print(*result)