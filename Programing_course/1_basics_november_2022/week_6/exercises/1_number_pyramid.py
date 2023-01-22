n = int(input())


is_equal = False
current = 1

for row in range(1, n + 1):
    for collumn in range(1, row + 1):
        print(current, end=" ")
        current += 1
        if current > n:
            is_equal = True
            break
    if is_equal:
        break

    print()
