elements = input().split()

result = {}

for el in elements:
    el_lower = el.lower()

    if el_lower in result:
        result[el_lower] += 1
    else:
        result[el_lower] = 1

for key, value in result.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")