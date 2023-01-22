stadium_capacity = int(input())
total_fan_count = int(input())

a_counter = 0
b_counter = 0
v_counter = 0
g_counter = 0


for _ in range(total_fan_count):
    fan_place = input()

    if fan_place == "A":
        a_counter += 1
    elif fan_place == "B":
        b_counter += 1
    elif fan_place == "V":
        v_counter += 1
    else:
        g_counter += 1

a_percent = a_counter / total_fan_count * 100
b_percent = b_counter / total_fan_count * 100
v_percent = v_counter / total_fan_count * 100
g_percent = g_counter / total_fan_count * 100
fan_percent = total_fan_count / stadium_capacity * 100

print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{fan_percent:.2f}%")