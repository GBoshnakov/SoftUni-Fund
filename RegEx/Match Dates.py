import re

text = input()

regex = r"\b(?P<day>\d{2})(?P<separator>[-.\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

result = [el.groupdict()for el in re.finditer(regex, text)]

#print('\n'.join([f"Day: {data['day']}, Month: {data['month']}, Year: {data['year']}" for data in result]))

for el in result:
     print( f"Day: {el['day']}, Month: {el['month']}, Year: {el['year']}")