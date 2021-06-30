elements = input().split()
total_sum = 0

for el in elements:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])

    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    else:
        total_sum += number * (ord(first_letter) - 96)

    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64
    else:
        total_sum += ord(last_letter) - 96

print(f"{total_sum:.2f}")