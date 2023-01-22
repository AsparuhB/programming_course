while True:
    input_line = input()
    if input_line == "End":
        break

    if input_line == "SoftUni":
        continue

    for ch in input_line:
        print(f"{ch}{ch}", end="")
    print()
