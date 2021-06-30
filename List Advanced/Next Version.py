version = [int(n) for n in input().split(".")]
part1 = version[0]
part2 = version[1]
part3 = version[2]

if part3 < 9:
    part3 += 1
else:
    part3 = 0
    if part2 < 9:
        part2 += 1
    else:
        part2 = 0
        if part1 < 9:
            part1 += 1

print(f"{part1}.{part2}.{part3}")