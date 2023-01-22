# Read Input
from math import ceil, floor


num_magnolias = int(input())
num_zumbules = int(input())
num_roses = int(input())
num_cacti = int(input())
price_present = float(input())


# Logic

magnolias_price = num_magnolias * 3.25
zumbules_price = num_zumbules * 4
roses_price = num_roses * 3.50
cacti_price = num_cacti * 8

total = magnolias_price + zumbules_price + roses_price + cacti_price
total -= total * 0.05

diff = abs(price_present - total)

# Output

if total >= price_present:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
