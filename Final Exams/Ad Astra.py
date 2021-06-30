import re
text = input()

regex = r"(#|\|)(?P<food>([A-Za-z\s]+))\1(?P<date>((\d{2}/){2}\d{2}))\1(?P<calories>([0-9]{1,4}|10000))\1"

total_calories = 0

items = [el.groupdict() for el in re.finditer(regex, text)]

for item in items:

    total_calories += int(item['calories'])

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for item in items:

    print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['calories']}")