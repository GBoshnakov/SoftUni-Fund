data = input()

submissions = {}
languages_count = {}

while data != "exam finished":
    data = data.split("-")
    if len(data) == 3:
        name, language, points = data
        points = int(points)

        if language not in languages_count:
            languages_count[language] = 0
        languages_count[language] += 1

        if name not in submissions:
            submissions[name] = {"language": language, "points": points}
        else:
            if language in submissions[name]["language"]:
                if points > submissions[name]["points"]:
                    submissions[name]["points"] = points
            else:
                submissions[name]["language"] = language
                submissions[name]["points"] = points
    elif len(data) == 2:
        name, command = data
        if command == "banned":
            del submissions[name]

    data = input()

sorted_submissions = sorted(submissions.items(), key=lambda kvp: (-kvp[1]["points"], kvp[0]))
sorted_language_count =sorted(languages_count.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print(f"Results:")
for key, val in sorted_submissions:
    print(f"{key} | {val['points']}")
print(f"Submissions:")
for key, val in sorted_language_count:
    print(f"{key} - {val}")

