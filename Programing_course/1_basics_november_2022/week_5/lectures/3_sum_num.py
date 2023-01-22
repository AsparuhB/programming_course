number = int(input())
total = 0

while True:
    num = int(input())
    total += num

    if total >= number:
        break

print(total)