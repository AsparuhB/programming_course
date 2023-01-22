money_per_day = float(input())
money_to_make_per_day = float(input())
total_expenses = float(input())
present_price = float(input())

days = 5

money_gathered_total = days * money_per_day
money_made_total = days * money_to_make_per_day

total_money_gathered = money_made_total + money_gathered_total

left_money = total_money_gathered - total_expenses

diff = abs(left_money - present_price)


if left_money >= present_price:
    print(f"Profit: {left_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")