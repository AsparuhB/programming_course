quantity = int(input())
days_till_christmas = int(input())

total_budget = 0
total_spirit = 0

for day in range(1, days_till_christmas + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_budget += 2 * quantity
        total_spirit += 5

    if day % 3 == 0:
        total_budget += 5 * quantity
        total_spirit += 3
        total_budget += 3 * quantity
        total_spirit += 10

    if day % 5 == 0:
        total_budget += 15 * quantity
        total_spirit += 17
        if day % 5 == 0 and day % 3 == 0:
            total_spirit += 30


    if day % 10 == 0:
        total_spirit -= 20
        total_budget += 23

if days_till_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_budget}")
print(f"Total spirit: {total_spirit}")
