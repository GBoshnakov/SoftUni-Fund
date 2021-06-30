names = input().split(", ")



for el in names:
    is_valid = True
    if len(el) in range(3, 17):
        for i in range(len(el)):
            if not (el[i].isalnum() or el[i] == "-" or el[i] == "_"):
                is_valid = False
                break
        if is_valid:
            print(el)
