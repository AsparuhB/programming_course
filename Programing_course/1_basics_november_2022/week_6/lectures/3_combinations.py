n = int(input())

combinations_counter = 0

for x1 in range(n + 1):
    for x2 in range(n + 2):
        for x3 in range(n + 3):
            if x1 + x2 + x3 == n:
                combinations_counter += 1

print(combinations_counter)
