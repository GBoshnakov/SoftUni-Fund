command = input()



temp_resource = []

resources = {}

while command != "stop":

    temp_resource.append(command)

    command = input()

for i in range(0, len(temp_resource,), 2):
    if temp_resource[i] not in resources:
        resources[temp_resource[i]] = 0
    resources[temp_resource[i]] += int(temp_resource[i + 1])


for k, v in resources.items():
    print(f"{k} -> {v}")

