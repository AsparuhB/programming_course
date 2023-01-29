duels_lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

times_shield_broken = 0
needed_aureus = 0

for duel in range(1, duels_lost + 1):
    if duel % 2 == 0:
        needed_aureus += helmet_price

    if duel % 3 == 0:
        needed_aureus += sword_price

    if duel % 2 == 0 and duel % 3 == 0:
        needed_aureus += shield_price
        times_shield_broken += 1
        if times_shield_broken % 2 == 0:
            needed_aureus += armor_price


print(f"Gladiator expenses: {needed_aureus:.2f} aureus")

