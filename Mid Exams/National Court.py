import math
person1 = int(input())
person2 = int(input())
person3 = int(input())

total_amount_of_people = int(input())

total_questions_per_hour = person1 + person2 + person3

time_needed = 0
extra_hours = 0

while total_amount_of_people > 0:
    time_needed += 1
    total_amount_of_people -= total_questions_per_hour

    if time_needed % 3 == 0 and total_amount_of_people != 0:
        extra_hours += 1
time_needed += extra_hours

print(f"Time needed: {time_needed}h.")