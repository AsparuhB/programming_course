factor = int(input())
count = int(input())

needed_numbers = []
iterations = 0

while True:
    iterations += 1
    if iterations % factor == 0:
        needed_numbers.append(iterations)

    if iterations >= factor * count:
        break

print(needed_numbers)