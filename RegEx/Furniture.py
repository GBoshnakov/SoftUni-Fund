import re

data = input()

regex = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

total_money = 0
items = []

while data != "Purchase":
    match = re.match(regex, data)
    if match:
        current_furniture = match.groupdict()
        total_money += float(current_furniture["price"]) * int(current_furniture["quantity"])
        items.append(current_furniture["furniture"])
    data = input()
print("Bought furniture:")
for el in items:
    print(el)
print(f"Total money spend: {total_money:.2f}")