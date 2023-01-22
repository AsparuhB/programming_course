# Read input

fuel_type = input().lower()
liters = int(input())

# Logic
if fuel_type == "gasoline" or fuel_type == "diesel" or fuel_type == "gas":
    if liters >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")