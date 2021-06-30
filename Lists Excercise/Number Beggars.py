string = input().split(", ")

number_beggers = int(input())

starting_index = 0


sum_beggers_money = []

for begger in range(number_beggers):
    current_sum = 0

    for i in range(starting_index, len(string), number_beggers):
        current_sum += int(string[i])
    sum_beggers_money.append(current_sum)
    starting_index += 1

print(sum_beggers_money)


