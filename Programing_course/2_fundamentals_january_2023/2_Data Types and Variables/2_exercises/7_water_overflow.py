times_water_is_poured = int(input())

capacity = 255
water_filled = 0


for pours in range(times_water_is_poured):
    water_added = int(input())

    if capacity < water_added:
        print("Insufficient capacity!")
        continue

    capacity -= water_added
    water_filled += water_added


print(water_filled)

