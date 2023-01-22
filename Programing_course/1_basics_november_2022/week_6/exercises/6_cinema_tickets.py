total_ticket_counter = 0
kid_counter = 0
student_counter = 0
standard_counter = 0

while True:
    input_line = input()
    if input_line == "Finish":
        break
    total_spaces = int(input())

    full_counter = 0
    while True:
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "kid":
            kid_counter += 1
            total_ticket_counter += 1
            full_counter += 1
        elif ticket_type == "student":
            student_counter += 1
            total_ticket_counter += 1
            full_counter += 1
        else:
            standard_counter += 1
            total_ticket_counter += 1
            full_counter += 1

        if full_counter == total_spaces:
            break

    free = full_counter / total_spaces * 100
    print(f"{input_line} - {free:.2f}% full.")

print(f"Total tickets: {total_ticket_counter}")
kid_percent = kid_counter / total_ticket_counter * 100
student_percent = student_counter / total_ticket_counter * 100
standard_percent = standard_counter / total_ticket_counter * 100

print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")