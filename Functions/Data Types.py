data_type = input()
if data_type == "int":
    value = int(input())
    result = value * 2
    print(result)
elif data_type == "real":
    value = float(input())
    result = value * 1.5
    print(f"{result:.2f}")
elif data_type == "string":
    value = input()
    print(f"${value}$")

