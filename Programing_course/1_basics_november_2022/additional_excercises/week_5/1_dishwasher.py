detergent_bottles = int(input())

detergent_ml = 750
total_detergent_ml = detergent_ml * detergent_bottles
detergent_needed = 0

dishes_counter = 0
pots_counter = 0

times_started = 0

while True:
    input_line = input()
    if input_line == "End":
        break
    input_line = int(input_line)
    times_started += 1

    if times_started % 3 == 0:
        detergent_needed += input_line * 15
        pots_counter += input_line
    else:
        detergent_needed += input_line * 5
        dishes_counter += input_line

    diff = total_detergent_ml - detergent_needed
    if diff < 0:
        print(f"Not enough detergent, {abs(diff)} ml. more necessary!")
        break

if diff >= 0:
    print("Detergent was enough!")
    print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {diff} ml.")

