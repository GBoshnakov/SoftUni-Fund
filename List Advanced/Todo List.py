todo_note = input()

text = [0] * 10


while not todo_note == "End":
    index, todo = todo_note.split("-")
    index = int(index) - 1

    text[index] = todo

    todo_note = input()


# text = [n for n in text if n != 0]
# print(text)

print([n for n in text if not n == 0])