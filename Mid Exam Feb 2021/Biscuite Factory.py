biscuits_per_day = int(input())

workers = int(input())

competing_factory = int(input())

total_biscuits = 0

for day in range(1, 30 + 1):
    daily_production = 0
    if day % 3 == 0:
        daily_production = int(biscuits_per_day * workers * 0.75)
        total_biscuits += daily_production
    else:
        daily_production = int(biscuits_per_day * workers)
        total_biscuits += daily_production

print(f"You have produced {total_biscuits} biscuits for the past month.")

difference = abs(total_biscuits - competing_factory)


if total_biscuits > competing_factory:
    print(f"You produce { difference/ competing_factory * 100:.2f} percent more biscuits.")
elif total_biscuits < competing_factory:
    print(f"You produce {difference / competing_factory * 100:.2f} percent less biscuits.")