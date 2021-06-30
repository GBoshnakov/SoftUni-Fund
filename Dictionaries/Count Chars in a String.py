data = input().split()
string = "".join(data)

count_in_dict = {}


for i in range(len(string)):
    if string[i] not in count_in_dict:
        count_in_dict[string[i]] = string.count(string[i])


for key, val in count_in_dict.items():
    print(f"{key} -> {val}")