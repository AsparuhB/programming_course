# Input
months = int(input())

water_bill = 20
internet_bill = 15

electricity_total = 0
water_total = 0
internet_total = 0
others_total = 0

# Logic

for _ in range(months):
    electricity_bill = float(input())

    electricity_total += electricity_bill
    water_total += 20
    internet_total += 15


    others = electricity_bill + water_bill + internet_bill
    others += others * 0.20
    others_total += others

average = (electricity_total + water_total + internet_total + others_total) / months

# Output
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {average:.2f} lv")
