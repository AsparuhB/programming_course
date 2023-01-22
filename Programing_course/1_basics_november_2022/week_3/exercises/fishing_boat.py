# Read Input

budged = int(input())
season = input()
fishermen = int(input())

# Logic // Spring = 3000, Summer, Autumn = 4200, Winter = 2600

price = 0
if season == "Spring":
    price += 3000
elif season == "Summer" or season == "Autumn":
    price += 4200
elif season == "Winter":
    price += 2600

if fishermen <= 6:
    price -= price * 0.10
elif 7 < fishermen <= 11:
    price -= price * 0.15
elif fishermen > 11:
    price -= price * 0.25

if fishermen % 2 == 0 and season != "Autumn":
    price -= price * 0.05

diff_num = abs(budged - price)

if budged >= price:
    print(f"Yes! You have {diff_num:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff_num:.2f} leva.")
