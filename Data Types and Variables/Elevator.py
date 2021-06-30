number_of_people = int(input())
elevator_capacity = int(input())

number_of_runs = (number_of_people // elevator_capacity)
if number_of_runs < 1:
    number_of_runs = 1
elif not number_of_people % elevator_capacity == 0:
        number_of_runs += 1

print(number_of_runs)