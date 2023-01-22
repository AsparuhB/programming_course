# Read Input

veg_price_in_kg = float(input())
fruit_price_in_kg = float(input())
veg_total_kg = float(input())
fruit_total_kg = float(input())

# Logic

fruit = fruit_total_kg * fruit_price_in_kg
veggies = veg_price_in_kg * veg_total_kg

total_in_lv = fruit + veggies
total_in_euro = total_in_lv / 1.94

print(f"{total_in_euro:.2f}")