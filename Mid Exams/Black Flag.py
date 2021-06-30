days = int(input())

plunder_per_day = int(input())

plunder_expected = float(input())

current_plunder = 0

for n in range(1, days + 1):
    current_plunder += plunder_per_day
    if n % 3 == 0:
        current_plunder += plunder_per_day / 2
    if n % 5 == 0:
        current_plunder *= 0.7

if current_plunder >= plunder_expected:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {current_plunder / plunder_expected * 100:.2f}% of the plunder.")