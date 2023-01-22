# Read input

groups_num = int(input())

# Logic

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for people in range(1, groups_num + 1):
    people_in_group = int(input())

    if people_in_group <= 5:
        g1 += people_in_group
    elif people_in_group <= 12:
        g2 += people_in_group
    elif people_in_group <= 25:
        g3 += people_in_group
    elif people_in_group <= 40:
        g4 += people_in_group
    else:
        g5 += people_in_group

total_people = g1 + g2 + g3 + g4 + g5

g1_percent = g1 / total_people * 100
g2_percent = g2 / total_people * 100
g3_percent = g3 / total_people * 100
g4_percent = g4 / total_people * 100
g5_percent = g5 / total_people * 100

# Output

print(f"{g1_percent:.2f}%")
print(f"{g2_percent:.2f}%")
print(f"{g3_percent:.2f}%")
print(f"{g4_percent:.2f}%")
print(f"{g5_percent:.2f}%")
