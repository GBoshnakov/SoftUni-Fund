number_of_students = int(input())
number_of_lectures = int(input())
initial_bonus = int(input())

best_bonus = 0
current_best = 0
current_attendances = int()

for n in range(number_of_students):

    student_attendances = int(input())
    best_bonus = round(student_attendances / number_of_lectures * (5 + initial_bonus))

    if best_bonus > current_best:
        current_best = best_bonus
        current_attendances = student_attendances


print(f"Max Bonus: {current_best}.")
print(f"The student has attended {current_attendances} lectures.")