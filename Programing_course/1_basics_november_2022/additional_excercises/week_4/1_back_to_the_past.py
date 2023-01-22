inherited_money = float(input())
year_to_live = int(input())

year_back = 1800
needed_money_per_year = 12000
age = 18

for year in range(year_back, year_to_live + 1):
    if year % 2 == 0:
        inherited_money -= needed_money_per_year
    else:
        inherited_money -= needed_money_per_year + age * 50
    age += 1

if inherited_money >= 0:
    print(f'Yes! He will live a carefree life and will have {(inherited_money):.2f} dollars left.')
else:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')