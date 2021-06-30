text_crypted = input().split()
list_new = []
for word in text_crypted:
    number = ""
    for letter in word:
        if letter.isdigit():
            number += letter
    first_letter = chr(int(number))
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    result = "".join(current_word)
    #print(f'{"".join(current_word)}', end=" ")
    list_new.append(result)
    #print(f"{result}", end=" ")



print(list_new)


print(f'{" ".join(list_new)}')