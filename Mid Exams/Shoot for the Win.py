targets = [int(n) for n in input().split()]

index = input()
shot_target = 0

while index != "End":
    index = int(index)

    if 0 <= index < len(targets):

        shot_target = targets[index]

        if targets[index] >= 0:
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > shot_target:
                        targets[i] -= shot_target
                    else:
                        targets[i] += shot_target

    index = input()

print(f'Shot targets: {targets.count(-1)} -> {" ".join(list(map(str, targets)))}')
