year = int(input())

year += 1

while True:
    year_in_str = str(year)
    if len(year_in_str) == len(set(year_in_str)):
        print(year)
        break
    year += 1
