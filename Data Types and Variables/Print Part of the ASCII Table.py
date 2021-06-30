starting_index = int(input())
ending_index = int(input())

chars = ""

for number in range (starting_index, ending_index + 1):
    chars = chars + " " + chr(number)

print(chars)

