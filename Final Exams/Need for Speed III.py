n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            filled_fuel = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {filled_fuel} liters")
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kiometers = int(command[2])
        if cars[car]["mileage"] - kiometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kiometers
            print(f"{car} mileage decreased by {kiometers} kilometers")

    command = input()

sorted_cars = sorted(cars.items(), key=lambda kvp:(-kvp[1]["mileage"], kvp[0]))
for key, val in sorted_cars:
    print(f"{key} -> Mileage: {val['mileage']} kms, Fuel in the tank: {val['fuel']} lt.")