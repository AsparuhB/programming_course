film_budged = float(input())
statists = int(input())
clothes_for_one_statist = float(input())

decor = film_budged * 0.10

total_sum_for_statists = statists * clothes_for_one_statist

if statists > 150:
    total_sum_for_statists = total_sum_for_statists - (total_sum_for_statists * 0.10)

total_money_needed = decor + total_sum_for_statists

diff = abs(film_budged - total_money_needed)

if film_budged >= total_money_needed:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")