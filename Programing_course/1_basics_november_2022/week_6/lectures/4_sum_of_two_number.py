starting_interval = int(input())
ending_interval = int(input())
magic_number = int(input())

counter = 0
flag = False


for a in range(starting_interval, ending_interval + 1):
    for b in range(starting_interval, ending_interval + 1):
        counter += 1
        if a + b == magic_number:
            print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")