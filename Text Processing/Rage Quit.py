text = input()

unique_message = ""
number_of_unique_symbols = 0
current_text = ""

for i in range(len(text)):
    if text[i].isalpha():
        current_text += text[i].upper()
        if text[i].upper() not in unique_message:
            number_of_unique_symbols += 1
    elif not text[i].isalnum():
        current_text += text[i]
        if text[i] not in unique_message:
            number_of_unique_symbols += 1
    elif text[i].isdigit():
        number = int(text[i])
        if i + 1 in range(len(text)) and text[i + 1].isdigit():
            number = int(text[i] + text[i + 1])

        unique_message += number * current_text
        current_text = ""

print(f"Unique symbols used: {number_of_unique_symbols}")
print(f"{unique_message}")