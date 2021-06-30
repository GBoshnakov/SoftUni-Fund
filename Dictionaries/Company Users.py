command = input()

company_employees = {}

while command != "End":
    company, employee = command.split(" -> ")
    if company not in company_employees:
        company_employees[company] = []
    if employee not in company_employees[company]:
        company_employees[company].append(employee)

    command = input()

company_employees = sorted(company_employees.items(), key= lambda kvp: kvp[0])

for key, val in company_employees:
    print(f"{key}")
    for el in val:
        print(f"-- {el}")