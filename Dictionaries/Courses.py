students = input()

courses = {}

while students != "end":
    language, name = students.split(" : ")

    if language not in courses:
        courses[language] = []
    courses[language].append(name)

    students = input()

sorted_courses = dict(sorted(courses.items(), key=lambda kvp: -len(kvp[1])))

for key, val in sorted_courses.items():
    sorted_courses[key] = list(sorted(val))

for key, val in sorted_courses.items():
    print(f"{key}: {len(val)}")
    for el in val:
        print(f"-- {el}")