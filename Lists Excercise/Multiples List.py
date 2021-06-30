factor = int(input())
count = int(input())

result = []

numbers = 1

#for num in range(count):
#    if num % factor == 0

while len(result) < count:
    if numbers % factor == 0:
        result.append(numbers)
    numbers += 1
print(result)




