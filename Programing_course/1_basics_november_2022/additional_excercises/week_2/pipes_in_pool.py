# Read Input

pool_volume = int(input())
p1_per_hour = int(input())
p2_per_hour = int(input())
not_there_time = float(input())

# Logic


p1_total_water = p1_per_hour * not_there_time
p2_total_water = p2_per_hour * not_there_time

total_water_init = p1_total_water + p2_total_water

water_in_volume = total_water_init / pool_volume * 100

# Output

if total_water_init <= pool_volume:
    p1_volume_percent = p1_total_water / total_water_init * 100
    p2_volume_percent = p2_total_water / total_water_init * 100
    print(f"The pool is {water_in_volume:.2f}% full. Pipe 1: {p1_volume_percent:.2f}%."
          f" Pipe 2: {p2_volume_percent:.2f}%. ")
else:
    diff = abs(pool_volume - total_water_init)
    print(f"For {not_there_time:.2f} hours the pool overflows with {diff:.2f} liters.")