n = int(input())



for number1 in range(n):
    for number2 in range(n):
        for number3 in range(n):
            print(chr(number1 + 97) + chr(number2 + 97) + chr(number3 + 97) )