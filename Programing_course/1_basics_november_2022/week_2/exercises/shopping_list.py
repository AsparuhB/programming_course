# Read Input

budged = float(input())
gpu_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

# Logic

gpu_price = 250
gpu = gpu_quantity * gpu_price
cpu_price = gpu * 0.35
ram_price = gpu * 0.10


cpu = cpu_price * cpu_quantity
ram = ram_price * ram_quantity

total = gpu + cpu + ram
if gpu_quantity > cpu_quantity:
    total -= total * 0.15

# Output
if budged >= total:
    print(f"You have {budged - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budged:.2f} leva more!")

