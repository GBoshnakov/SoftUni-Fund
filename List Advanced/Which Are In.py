list_1 = input().split(", ")

list_2 = input().split(", ")


result = [word for word in list_1 if any(word in s for s in list_2)]


print(result)

