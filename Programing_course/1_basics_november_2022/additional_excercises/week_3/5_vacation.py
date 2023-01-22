# Read Input

budged = float(input())
season = input()

# Logic
destination = ""
site = ""
total = 0

if budged <= 1000:
    site = "Camp"
    if season == "Summer":
        destination = "Alaska"
        total += budged * 0.65
    elif season == "Winter":
        destination = "Morocco"
        total += budged * 0.45
elif budged <= 3000:
    site = "Hut"
    if season == "Summer":
        destination = "Alaska"
        total += budged * 0.80
    elif season == "Winter":
        destination = "Morocco"
        total = budged * 0.60
else:
    site = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        total += budged * 0.90
    elif season == "Winter":
        destination = "Morocco"
        total += budged * 0.90

# Output

print(f"{destination} - {site} - {total:.2f}")
