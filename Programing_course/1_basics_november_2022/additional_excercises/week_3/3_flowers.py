# Read input

chrysanthemum_number = int(input())
roses_number = int(input())
tulip_number = int(input())
season = input().lower()  # Spring, Summer, Autumn, Winter
holiday = input().lower()  # Y - Yes // N - No

# Logic

chrysanthemums = 0
roses = 0
tulips = 0
arrange = 2

total_number = chrysanthemum_number + roses_number + tulip_number

if season == "spring":
    chrysanthemums += 2
    roses = 4.10
    tulips = 2.50
    total = chrysanthemum_number * chrysanthemums + roses_number * roses + tulip_number * tulips
    if holiday == "y":
        total += total * 0.15
    if tulip_number > 7:
        total -= total * 0.05
    if total_number > 20:
        total -= total * 0.20
elif season == "summer":
    chrysanthemums += 2
    roses = 4.10
    tulips = 2.50
    total = chrysanthemum_number * chrysanthemums + roses_number * roses + tulip_number * tulips
    if holiday == "y":
        total += total * 0.15
    if total_number > 20:
            total -= total * 0.20
elif season == "autumn":
    chrysanthemums += 3.75
    roses = 4.50
    tulips = 4.15
    total = chrysanthemum_number * chrysanthemums + roses_number * roses + tulip_number * tulips
    if holiday == "y":
        total += total * 0.15
    if total_number > 20:
            total -= total * 0.20
elif season == "winter":
    chrysanthemums += 3.75
    roses = 4.50
    tulips = 4.15
    total = chrysanthemum_number * chrysanthemums + roses_number * roses + tulip_number * tulips
    if holiday == "y":
        total += total * 0.15
    if roses_number >= 10:
        total -= total * 0.10
    if total_number > 20:
            total -= total * 0.20


total = total + arrange


# Output
print(f"{total:.2f}")
