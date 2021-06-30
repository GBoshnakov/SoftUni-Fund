def calc_factorial(num):
    factorial = 1
    for n in range (2, num + 1):
        factorial *= n

    return factorial

num1 = int(input())
num2 = int(input())

result = calc_factorial(num1) / calc_factorial(num2)

print(f"{result:.2f}")