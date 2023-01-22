did_go = False
while True:
    destination = input()
    if destination == "End":
        did_go = True
        break
    vacation_budged = float(input())
    budged = 0

    while True:
        budged_needed = float(input())
        budged += budged_needed
        if budged >= vacation_budged:
            print(f"Going to {destination}!")
            break
