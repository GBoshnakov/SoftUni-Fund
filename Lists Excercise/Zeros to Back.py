string = input().split(", ")
list_as_int = list(map(int, string))

for i in range(len(list_as_int)):
    if list_as_int[i] == 0:
        list_as_int.remove(list_as_int[i])
        list_as_int.append(0)


print(list_as_int)

