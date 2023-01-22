# Read Input

car_budged = float(input())
season = input()  # Summer and Winter

total = 0
car_class = ""
car_type = ""

# Logic

if car_budged <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        total += car_budged * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        total += car_budged * 0.65
elif car_budged <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        total += car_budged * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        total += car_budged * 0.80
elif car_budged > 500:
    car_type = "Jeep"
    car_class = "Luxury class"
    total += car_budged * 0.90

# Output

print(f"{car_class}")
print(f"{car_type} - {total:.2f}")
