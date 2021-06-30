import re

n = int(input())

regex = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

for num in range(n):
    text = input()
    match = re.match(regex, text)
    if not match:
        print(f"Invalid barcode")
    else:
        item = match.group()
        barcode = ""
        for el in item:
            if el.isdigit():
                barcode += el

        if not barcode:
            print(f"Product group: 00")
        else:
            print(f"Product group: {barcode}")




