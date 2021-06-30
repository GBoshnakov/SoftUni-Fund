import re

text = input()

regex = r"\d+"

result = []

while text:


    result.extend([el.group() for el in re.finditer(regex, text)])





    text = input()

print(*result)
