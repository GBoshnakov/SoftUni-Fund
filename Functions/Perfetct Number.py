def check_if_perfect(num):
    list_of_divisors = []
    for n in range(1, num):
        if num % n == 0:
            list_of_divisors.append(n)

    if sum(list_of_divisors) == num:

        return True
    return False

number = int(input())

result =  check_if_perfect(number)
if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

