#Read Input
movie_budged = float(input())
statists = int(input())
suits_price = float(input())

#Logic

decor = movie_budged * 0.1
if statists > 150:
    suits_price -= suits_price * 0.10

total_expence = statists * suits_price + decor

#Output
if movie_budged < total_expence:
    print("Not enough money!")
    print(f"Wingard needs {total_expence - movie_budged:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budged - total_expence:.2f} leva left.")
