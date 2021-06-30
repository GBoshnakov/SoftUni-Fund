import re
racers = [m for m in input().split(", ")]
data = input()
regex = r"[a-zA-Z0-9]"

results = {}


while data != "end of race":
    current_racer = ""
    current_distance = 0
    matches = re.findall(regex, data)
    for el in matches:
        if el.isdigit():
            current_distance += int(el)
        elif el.isalpha():
            current_racer += el
    if current_racer in racers:
        if current_racer not in results:
            results[current_racer] = 0
        results[current_racer] += current_distance


    data = input()
sorted_results = sorted(results.items(), key=lambda kvp: -kvp[1])
counter = 1
for key, val in sorted_results:
    if counter ==4:
        break
    if counter == 1:
        print(f"{counter}st place: {key}")
    elif counter == 2:
        print(f"{counter}nd place: {key}")
    elif counter == 3:
        print(f"{counter}rd place: {key}")
    counter += 1

