
year_tax = int(input())
shoes_price = year_tax - (year_tax * 0.40)
jersey_price = shoes_price - (shoes_price * 0.20)
bascet_ball = jersey_price / 4
bascetball_acc = bascet_ball / 5

total = year_tax + shoes_price + jersey_price + bascet_ball + bascetball_acc

print(total)