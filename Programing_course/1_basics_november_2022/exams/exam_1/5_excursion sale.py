number_sea_vacations = int(input())
number_mountain_vacations = int(input())


sea_vacation_counter = number_sea_vacations
mountain_vacation_counter = number_mountain_vacations

total_profit = 0
while True:
    command = input().lower() #sea - 680, mountain - 499 or Stop
    if command == "stop":
        break

    if command == "sea":
        if sea_vacation_counter == 0:
            pass
        else:
            sea_vacation_counter -= 1
            total_profit += 680

    elif command == "mountain":
        if mountain_vacation_counter == 0:
            pass
        else:
            mountain_vacation_counter -= 1
            total_profit += 499

    if sea_vacation_counter == 0 and mountain_vacation_counter == 0:
        break

if sea_vacation_counter == 0 and mountain_vacation_counter == 0:
    print(f"Good job! Everything is sold.")
    print(f"Profit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
