def odd_and_even_sum(a):
    sum_odds = 0
    sum_evens = 0
    for n in a:
        if int(n) % 2 == 0:
            sum_evens += int(n)
        else:
            sum_odds += int(n)
    return str(sum_odds), str(sum_evens)
number = input()


sum_odds, sum_evens = odd_and_even_sum(number)
print(f"Odd sum = {sum_odds}, Even sum = {sum_evens}")
