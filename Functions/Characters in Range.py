def chars_in_range_ASCII(a, b):
    result = []
    for n in range(ord(a) + 1, ord(b)):

        text = ""
        result.append(chr(n))
    text = " ".join(result)

    return text

x = input()
y = input()


print(chars_in_range_ASCII(x, y))

