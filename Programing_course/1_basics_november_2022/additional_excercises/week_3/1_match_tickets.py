# Read input

budged = float(input())
ticket_category = input().lower()
people_in_group = int(input())

ticket_price = 0
transport = 0

# Logic

if ticket_category == "vip":
    ticket_price += 499.99
elif ticket_category == "normal":
    ticket_price += 249.99

if 1 <= people_in_group <= 4:
    transport = budged * 0.75
elif 5 <= people_in_group < 10:
    transport = budged * 0.60
elif 10 <= people_in_group < 25:
    transport = budged * 0.50
elif 25 <= people_in_group < 50:
    transport = budged * 0.40
elif people_in_group >= 50:
    transport = budged * 0.25


left = budged - transport
tickets = ticket_price * people_in_group

# Output

if left > tickets:
    print(f"Yes! You have {left - tickets:.2f} leva left.")
elif left < tickets:
    print(f"Not enough money! You need {tickets - left:.2f} leva.")
