n = int(input())
import sys

best_snowball = -sys.maxsize
best_snowball_snow = int()
best_snowball_time = int()
best_snowball_quality = int()
best_snowball_value = int()

for number in range (1, n+1):

    snowball_value = 0

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if best_snowball < snowball_value:
        best_snowball = snowball_value
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
        best_snowball_value = snowball_value



print(f'{best_snowball_snow} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})')