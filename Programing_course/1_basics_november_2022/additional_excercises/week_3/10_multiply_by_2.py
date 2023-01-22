is_positive = False

while True:
    current_num = float(input())
    if current_num >= 0:
        total = current_num * 2
        print(f"Result: {total:.2f}")
    else:
        print("Negative number!")
        break