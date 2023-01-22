#Read input

vacation_price = float(input())
num_puzzle = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

#Logic

total = num_puzzle * 2.60
total += num_dolls * 3
total += num_bears * 4.10
total += num_minions * 8.20
total += num_trucks * 2

num_toys = num_puzzle + num_dolls + num_bears + num_minions + num_trucks
if num_toys >= 50:
    total -= total * 0.25
total -= total * 0.1

#output

if total >= vacation_price:
    print(f"Yes! {total - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total:.2f} lv needed.")




