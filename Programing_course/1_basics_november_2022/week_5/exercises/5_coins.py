# Read input

change = float(input())

coins_change = change * 100

coin_counter = 0

while True:
    if coins_change >= 200:
        coins_change -= 200
    elif coins_change >= 100:
        coins_change -= 100
    elif coins_change >= 50:
        coins_change -= 50
    elif coins_change >= 20:
        coins_change -= 20
    elif coins_change >= 10:
        coins_change -= 10
    elif coins_change >= 5:
        coins_change -= 5
    elif coins_change >= 2:
        coins_change -= 2
    elif coins_change >= 1:
        coins_change -= 1
    else:
        break

    coin_counter += 1

    if coins_change == 0:
        break

print(coin_counter)