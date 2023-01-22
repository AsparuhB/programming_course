# Read Input

budged = float(input())
season = input().lower()

# Logic
destination = ""
place = ""
price = 0

if budged <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budged * 0.30
    elif season == "winter":
        place = "Hotel"
        price = budged * 0.70

elif budged <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budged * 0.40
    elif season == "winter":
        place = "Hotel"
        price = budged * 0.80

elif budged > 1000:
    destination = "Europe"
    place = "Hotel"
    price = budged * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")