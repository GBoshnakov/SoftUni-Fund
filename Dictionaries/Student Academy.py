from statistics import mean
n = int(input())

student_grades = {}

for student in range(n):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for key, val in student_grades.items():
    student_grades[key] = mean(val)


filtered_grades = sorted(student_grades.items(), key= lambda kvp: -kvp[1])

for key, val in filtered_grades:
    if val >= 4.5:
        print(f"{key} -> {val:.2f}")