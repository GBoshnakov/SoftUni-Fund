def loading_bar(num):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    num //= 10
    for index in range(num):
        bar[index] = "%"

    return "".join(bar)

number = int(input())

result_bar = loading_bar(number)

if result_bar.count("%") == 10:
    print(f"{number}% Complete!")
    print(f"[{result_bar}]")
else:
    print(f"{number}% [{result_bar}]")
    print("Still loading...")