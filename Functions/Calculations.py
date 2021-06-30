def calculation(a, b, string):
    if string == "multiply":
        return a * b
    elif string == "divide":
        return a // b
    elif string == "add":
        return a + b
    elif string == "subtract":
        return a - b

text = input()

num1 = int(input())
num2 = int(input())



result = calculation(num1, num2, text)
print(result)