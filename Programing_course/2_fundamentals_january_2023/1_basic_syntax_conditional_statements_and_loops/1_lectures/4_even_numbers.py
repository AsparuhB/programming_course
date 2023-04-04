num = int(input())

for i in range(num):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")