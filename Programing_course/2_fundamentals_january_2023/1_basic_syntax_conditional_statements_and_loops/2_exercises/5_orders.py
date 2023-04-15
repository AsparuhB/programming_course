number_of_orders = int(input())

total = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    current_order = 0

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        current_order += price_per_capsule * capsules_per_day * days
        print(f"The price for the coffee is: ${current_order:.2f}")
        total += current_order


print(f"Total: ${total:.2f}")