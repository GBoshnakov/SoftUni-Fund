employees = [int(n) for n in input().split()]


factor = int(input())

mapped_emplyees = list(map(lambda x: x * factor, employees))
average_happines = sum(mapped_emplyees) / len(mapped_emplyees)

happy_employees = list(filter(lambda x: x >= average_happines, mapped_emplyees))



if len(mapped_emplyees) / 2 <= len(happy_employees):
    print(f"Score: {len(happy_employees)}/{len(mapped_emplyees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(mapped_emplyees)}. Employees are not happy!")


