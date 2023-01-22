# Read input

num_kilometers = int(input())
day_or_night = input().lower()

total = 0

# Logic

if num_kilometers < 20:
    total += 0.70
    if day_or_night == "day":
        total += num_kilometers * 0.79
    elif day_or_night == "night":
        total += num_kilometers * 0.90
elif num_kilometers < 100:
    total += num_kilometers * 0.09

elif num_kilometers >= 100:
    total += num_kilometers * 0.06

# Output

print(f"{total:.2f}")
