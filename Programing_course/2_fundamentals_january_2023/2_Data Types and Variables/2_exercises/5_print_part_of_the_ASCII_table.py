starting_number = int(input())
ending_number = int(input())

for digit in range(starting_number, ending_number + 1):
    print(chr(digit), end=" ")