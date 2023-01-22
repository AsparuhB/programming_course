divisor = int(input())

boundary = int(input())

for num in range(boundary, 1, -1):
    if num % divisor == 0:
        print(num)
        exit()