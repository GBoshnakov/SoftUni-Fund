path = input()

file_name = ""
searched_file = []

for i in range(len(path) - 1, -1, -1):
    if path[i] == "\\":
        searched_file = path[i + 1:]
        break
file, extension = searched_file.split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")