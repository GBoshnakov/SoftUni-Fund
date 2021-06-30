n = int(input())

registered_cars = {}

for n in range(n):
    data = input().split()
    command = data[0]
    name = data[1]
    if command == "register":
        number_plate = data[2]
        if name not in registered_cars:
            registered_cars[name] = number_plate
            print(f"{name} registered {number_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {number_plate}")

    elif command == "unregister":
        if name not in registered_cars:
            print(f"ERROR: user {name} not found")
        else:
            registered_cars.pop(name)
            print(f"{name} unregistered successfully")

for key, value in registered_cars.items():
    print(f"{key} => {value}")