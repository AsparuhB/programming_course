number_to_be_added = int(input())

result = 0

for _ in range(number_to_be_added):
    current_letter = input()

    result += ord(current_letter)


print(f"The sum equals: {result}")
