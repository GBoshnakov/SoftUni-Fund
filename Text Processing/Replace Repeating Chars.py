text = input()

cut_text = ""

for i in range(0, len(text) - 1):
    if text[i] != text[i + 1]:
        cut_text += text[i]
    if i == len(text) - 2:
        cut_text += text[len(text) - 1]
print(cut_text)