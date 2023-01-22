# Read Input

seat_type = input().lower()
row = int(input())
collumn = int(input())

# Logic

seats = row * collumn

price = 0

if seat_type == "premiere":
    price += 12
elif seat_type == "normal":
    price += 7.50
elif seat_type == "discount":
    price += 5

# Output

total = seats * price

print(f"{total:.2f} leva")