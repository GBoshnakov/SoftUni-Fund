def sum_numbers(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def add_and_subtract(num1, num2, num3):
    return sum_numbers(a, b) - subtract(sum_numbers(a, b), c)


a = int(input())
b = int(input())
c = int(input())

print(subtract(sum_numbers(a, b), c))