prime_counter = 0
non_prime_counter = 0

while True:
    command_line = input()

    if command_line == "stop":
        break
    else:
        command_line = int(command_line)

    if command_line < 0:
        print("Number is negative.")
        continue

    divisior = 0
    for i in range(1, command_line + 1):
        if command_line % i == 0:
            divisior += 1


    if divisior > 2:
        non_prime_counter += command_line
    else:
        prime_counter += command_line

print(f"Sum of all prime numbers is: {prime_counter}")
print(f"Sum of all non prime numbers is: {non_prime_counter}")