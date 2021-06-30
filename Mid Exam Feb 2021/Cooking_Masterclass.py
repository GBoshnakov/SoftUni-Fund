import math
budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input())
apron_price = float(input())

student_set = 0
#student_set = flour_price + eggs_price * 10 + apron_price * 1.2

for _ in range(1, students + 1):
    if _ % 5 == 0:
        student_set += (eggs_price * 10)
    else:
        student_set += flour_price + (eggs_price * 10)
student_set += apron_price * math.ceil(students * 1.2)

money = abs(student_set - budget)

if student_set <= budget:
    print(f"Items purchased for {student_set:.2f}$.")
else:
    print(f"{money:.2f}$ more needed.")
