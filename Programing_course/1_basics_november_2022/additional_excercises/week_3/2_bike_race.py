# Read input

bikers_junior = int(input())
bikers_senior = int(input())
route = input().lower() # trail", "cross-country", "downhill" or "road"

# Logic

junior = 0
senior = 0

if route == "trail":
    junior += 5.50
    senior += 7
elif route == "cross-country":
    junior += 8
    senior += 9.50
    if (bikers_senior + bikers_junior) >= 50:
        junior -= junior * 0.25
        senior -= senior * 0.25
elif route == "downhill":
    junior += 12.25
    senior += 13.75
elif route == "road":
    junior += 20
    senior += 21.50

total = bikers_junior * junior + bikers_senior * senior
total -= total * 0.05

# Output

print(f"{total:.2f}")
