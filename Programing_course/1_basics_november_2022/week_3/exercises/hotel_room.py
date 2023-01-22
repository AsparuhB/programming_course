# Read input

month = input().lower()  # May, June, July, August, September or October
nights = int(input())

# Logic

studio = 0
apartment = 0
if month in ["may", "october"]:
    studio = 50
    if nights > 14:
        studio -= studio * 0.30
    elif nights > 7:
        studio -= studio * 0.05
    apartment = 65
    if nights > 14:
        apartment -= apartment * 0.10
elif month in ["june", "september"]:
    studio = 75.20
    if nights > 14:
        studio -= studio * 0.20
    apartment = 68.70
    if nights > 14:
        apartment -= apartment * 0.10
elif month in ["july", "august"]:
    studio = 76
    apartment = 77
    if nights > 14:
        apartment -= apartment * 0.10


#Output
print(f"Apartment: {apartment * nights:.2f} lv.")
print(f"Studio: {studio * nights:.2f} lv.")