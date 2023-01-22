# Read input
from math import ceil, floor


days_away = int(input())
food_left_in_kg = int(input())
dog_eats_kg = float(input())
cat_eats_kg = float(input())
turtle_eats_grams = float(input())

# Logic

dog_total = dog_eats_kg * days_away
cat_total = cat_eats_kg * days_away
turtle_total = turtle_eats_grams * days_away / 1000

total_food_needed = dog_total + cat_total + turtle_total

diff = abs(total_food_needed - food_left_in_kg)

# Output

if food_left_in_kg >= total_food_needed:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")