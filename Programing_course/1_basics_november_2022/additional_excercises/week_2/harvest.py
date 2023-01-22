# Read input
from math import ceil, floor


sqr_m_grape = int(input())
grape_for_one_sqrm = float(input())
liters_wine_needed = int(input())
num_workers = int(input())

# Logic

total_grape = sqr_m_grape * grape_for_one_sqrm
total_grape_for_wine = total_grape * 40 / 100
total_wine = total_grape_for_wine / 2.5

diff = abs(total_wine - liters_wine_needed)

# Output

if total_wine >= liters_wine_needed:
    liters_per_person = diff / num_workers
    print(f"Good harvest this year! Total wine: {ceil(total_wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(liters_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")





