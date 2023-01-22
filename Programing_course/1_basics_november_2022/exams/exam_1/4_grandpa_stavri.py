brew_days = int(input())


total_rakia = 0
total_rakia_degrees = 0

for brew in range(1, brew_days + 1):
    rakia_quantity = float(input())
    rakia_degrees = float(input())

    total_rakia += rakia_quantity
    total_rakia_degrees += rakia_quantity * rakia_degrees


degrees_per_liter = total_rakia_degrees / total_rakia

if degrees_per_liter < 38:
    print(f"Liter: {total_rakia:.2f}")
    print(f"Degrees: {degrees_per_liter:.2f}")
    print("Not good, you should baking!")

elif degrees_per_liter <= 42:
    print(f"Liter: {total_rakia:.2f}")
    print(f"Degrees: {degrees_per_liter:.2f}")
    print("Super!")
elif degrees_per_liter > 42:
    print(f"Liter: {total_rakia:.2f}")
    print(f"Degrees: {degrees_per_liter:.2f}")
    print("Dilution with distilled water!")

