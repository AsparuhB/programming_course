# Read Input

money_for_vacation = float(input())
available_money = float(input())

init_sum = available_money

spend_counter = 0
days_passed = 0
money_gathered = False

while True:
    financial_choice = input().lower()
    choice_quantity = float(input())
    days_passed += 1

    if financial_choice == "save":
        init_sum += choice_quantity
        spend_counter = 0

    elif financial_choice == "spend":
        init_sum -= choice_quantity
        spend_counter += 1
        if init_sum < 0:
            init_sum = 0

    if spend_counter >= 5:
        break

    if init_sum >= money_for_vacation:
        money_gathered = True
        break

if money_gathered:
    print(f"You saved the money for {days_passed} days.")
else:
    print(f"You can't save the money.")
    print(f"{days_passed}")

# Fuck me... Need to read more...
# Cannot be making stupid mistakes like this. The type of the number was shown at 5 different places, but I didn't
# pay attention. If I want to make it, this cannot continue.

#Focus. Focus. Focus. Focus

