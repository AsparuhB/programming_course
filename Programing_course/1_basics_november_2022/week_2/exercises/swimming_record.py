from math import floor

# Read Input

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())

# Logic

swimming_in_seconds = distance_in_meters * time_for_one_meter
swimming_delay = (floor(distance_in_meters / 15) * 12.5)

# total_time = swimming_in_seconds + swimming_delay
swimming_in_seconds += swimming_delay

# Output

if swimming_in_seconds < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {swimming_in_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {swimming_in_seconds - record_in_seconds:.2f} seconds slower.")
