import re
n = int(input())
regex = r"(\*|@)(?P<tag>[A-Z][a-z]{2,})\1:\s\[(?P<first>[A-Za-z])\]\|\[(?P<second>[A-Za-z])\]\|\[(?P<third>[A-Za-z])\]\|$"

for _ in range(n):
    text = input()

    matches = [el.groupdict() for el in re.finditer(regex, text)]

    #match = re.match(regex, text)


    if matches:
        for el in matches:
        #match = match.groupdict()
            print(f"{el['tag']}: {ord(el['first'])} {ord(el['second'])} {ord(el['third'])}")

    else:
        print("Valid message not found!")

    #print(matches)