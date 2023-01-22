number_of_orders = int(input())


total = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    order_price = capsules_per_day * days * price_per_capsule
    total += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")
