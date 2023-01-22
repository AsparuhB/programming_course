rent_room = float(input())

cake_price = rent_room * 0.20
drinks_price =cake_price - cake_price * 0.45
animator = rent_room / 3

budged = rent_room + cake_price + drinks_price + animator

print(budged)