# Read input

season = input()
kilometers_per_month = float(input())

# Logic
pay = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        pay += kilometers_per_month * 0.75 * 4
    elif season == "Summer":
        pay += kilometers_per_month * 0.90 * 4
    elif season == "Winter":
        pay += kilometers_per_month * 1.05 * 4

elif kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        pay += kilometers_per_month * 0.95 * 4
    elif season == "Summer":
        pay += kilometers_per_month * 1.10 * 4
    elif season == "Winter":
        pay += kilometers_per_month * 1.25 * 4

else:
    pay += kilometers_per_month * 1.45 * 4

pay_after_taxes = pay - pay * 0.10

# Output

print(f"{pay_after_taxes:.2f}")
