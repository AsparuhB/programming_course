divisor = int(input())
boundary = int(input())

max_div = 0

for number in range(1, boundary + 1):
    if number % divisor == 0:
        max_div = number

print(max_div)