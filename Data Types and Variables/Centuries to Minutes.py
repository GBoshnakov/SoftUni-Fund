centuries = int(input())
from math import floor

years = floor(100 * centuries)
days = floor(365.2422 * years)
hours = floor(24 * days)
minutes = floor(60 * hours)

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')