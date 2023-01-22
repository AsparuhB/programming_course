#input
number = int(input())
bonus = 0

#logic
if number > 1000:
    bonus += number * 0.10
elif number > 100:
    bonus += number * 0.20
if number <= 100:
    bonus += 5

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

#Output
print(bonus)
print(number + bonus)