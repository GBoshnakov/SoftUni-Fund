import re
n = int(input())
#pattern = r'(?P<username>U\$)[A-Z][a-z]{3,}\1(?P<password>P@\$)[A-z]{5,}[0-9]+(?P=password)'
#pattern = r"\U\$)(?P<username>[A-Z][a-z]{3,})\1(P@\$)(?P<password>[A-z]{5,}[0-9]+)(P@\$)"
pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})\1P@\$(?P<password>[A-z]{5,}[0-9]+)P@\$"
#pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})\1(P@\$)(?P<password>[a-zA-Z]{5,}[0-9]+)(P@\$)"

count = 0

for _ in range(n):

    registration = input()
    matches = [el.groupdict() for el in re.finditer(pattern, registration)]

    if matches:
        count += 1
        for el in matches:
            print('Registration was successful')
            print(f"Username: {el['username']}, Password: {el['password']}")

    else:
        print('Invalid username or password')

print(f"Successful registrations: {count}")
