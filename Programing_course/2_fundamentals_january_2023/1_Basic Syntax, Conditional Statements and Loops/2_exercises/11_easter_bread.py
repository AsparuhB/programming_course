budged = float(input())
flour_price_for_kg = float(input())
eggs_pack_price = flour_price_for_kg * 0.75
liter_milk_price = flour_price_for_kg + (flour_price_for_kg * 0.25)

money_needed_for_one_loaf = flour_price_for_kg + eggs_pack_price + (liter_milk_price / 4)

loaf_counter = 0
colored_eggs_counter = 0


while True:

    budged -= money_needed_for_one_loaf
    if budged <= 0:
        budged += money_needed_for_one_loaf
        print(f"You made {loaf_counter} loaves of Easter bread! "
              f"Now you have {colored_eggs_counter} eggs and {budged:.2f}BGN left.")
        break

    loaf_counter += 1
    colored_eggs_counter += 3

    if loaf_counter % 3 == 0:
        colored_eggs_counter -= loaf_counter - 2
