# Read Input

fuel_types = input()
fuel_quantity = float(input())
has_club_card = input()

# Logic

price = 0

if fuel_types == "Gas":
    price += 0.93
elif fuel_types == "Gasoline":
    price += 2.22
elif fuel_types == "Diesel":
    price += 2.33


if has_club_card == "Yes":
    if fuel_types == "Gasoline":
        price -= 0.18
    elif fuel_types == "Diesel":
        price -= 0.12
    elif fuel_types == "Gas":
        price -= 0.08

total = price * fuel_quantity

if 20 < fuel_quantity <= 25:
    total -= total * 0.08
elif fuel_quantity > 25:
    total -= total * 0.10

# Output

print(f"{total:.2f} lv.")
