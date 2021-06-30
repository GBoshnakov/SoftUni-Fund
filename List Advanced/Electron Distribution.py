number_of_electrons = int(input())

filled_shells = []
shell_counter = 1

while number_of_electrons  > 0:
    if number_of_electrons - 2 * shell_counter ** 2 >= 0:
        filled_shells.append(2 * shell_counter ** 2)
        number_of_electrons -= 2 * shell_counter ** 2
        shell_counter += 1
    else:
        filled_shells.append(number_of_electrons)
        number_of_electrons = 0


print(filled_shells)