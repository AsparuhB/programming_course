# Read Input

age = int(input())
washer_price = float(input())
toy_price = int(input())

# Logic

money = 0
total_money = 0
brother_money = 0
toy_counter = 0

for n in range(1, age + 1):
    if n % 2 != 0:
        toy_counter += 1

    else:
        money = money + 10
        total_money += money
        brother_money += 1

total_saved = total_money + (toy_counter * toy_price) - brother_money

diff = abs(washer_price - total_saved)

# Output

if total_saved >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
