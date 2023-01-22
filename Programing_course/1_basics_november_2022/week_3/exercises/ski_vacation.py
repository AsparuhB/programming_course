# Read input

days_stayed = int(input())
room_type = input().lower()  # room for one person, apartment, president apartment
rating = input().lower()

# Logic

price = 0

if room_type == "room for one person":
    price += 18
    total_stay = (days_stayed - 1) * price
elif room_type == "apartment":
    price += 25
    total_stay = (days_stayed - 1) * price
    if days_stayed < 10:
        total_stay -= total_stay * 0.30
    elif 10 <= days_stayed <= 15:
        total_stay -= total_stay * 0.35
    elif days_stayed > 15:
        total_stay -= total_stay * 0.50
elif room_type == "president apartment":
    price += 35
    total_stay = (days_stayed - 1) * price
    if days_stayed < 10:
        total_stay -= total_stay * 0.10
    elif 10 <= days_stayed <= 15:
        total_stay -= total_stay * 0.15
    elif days_stayed > 15:
        total_stay -= total_stay * 0.20

if rating == "positive":
    total_stay += total_stay * 0.25
elif rating == "negative":
    total_stay -= total_stay * 0.10


print(f"{total_stay:.2f}")
