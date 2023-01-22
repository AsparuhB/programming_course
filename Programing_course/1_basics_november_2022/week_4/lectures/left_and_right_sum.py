numbers = int(input())

num = 0
left_sum = 0
right_sum = 0

for num in range(numbers):
    left_sum += int(input())

for num in range(numbers):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")