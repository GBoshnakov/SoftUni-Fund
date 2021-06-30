numbers = [int(n) for n in input().split(", ")]

group = 10


while numbers:
    elements = []
    for el in numbers:
        if el <= group:
            elements.append(el)
    for el in elements:
        numbers.remove(el)

    print(f"Group of {group}'s: {elements}")

    group += 10