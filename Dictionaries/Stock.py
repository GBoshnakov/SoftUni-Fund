elements = input().split()

bakery = {}

for i in range(0, len(elements),2):
    key = elements[i]
    value = int(elements[i + 1])

    bakery[key] = value

searched_elements = input().split()

for el in searched_elements:
    if el in bakery:
        print(f"We have {bakery[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")