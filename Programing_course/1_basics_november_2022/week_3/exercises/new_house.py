# Read Input

flower_type = input()
flower_quantity = int(input())
budged = int(input())

# Logic

price = 0

if flower_type == "Roses":
    price += 5
    total_sum = flower_quantity * price
    if flower_quantity > 80:
        total_sum -= total_sum * 0.10

elif flower_type == "Dahlias":
    price += 3.80
    total_sum = flower_quantity * price
    if flower_quantity > 90:
        total_sum -= total_sum * 0.15

elif flower_type == "Tulips":
    price += 2.80
    total_sum = flower_quantity * price
    if flower_quantity > 80:
        total_sum -= total_sum * 0.15

elif flower_type == "Narcissus":
    price += 3
    total_sum = flower_quantity * price
    if flower_quantity < 120:
        total_sum += total_sum * 0.15

elif flower_type == "Gladiolus":
    price += 2.50
    total_sum = flower_quantity * price
    if flower_quantity < 80:
        total_sum += total_sum * 0.20
else:
    total_sum = flower_quantity * price

diff_num = abs(total_sum - budged)

if budged >= total_sum:

    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {diff_num:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff_num:.2f} leva more.")
