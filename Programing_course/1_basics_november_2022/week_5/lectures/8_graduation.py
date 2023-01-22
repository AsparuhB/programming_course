student_name = input()

total_grades_sum = 0
class_counter = 0
fail_counter = 0

while True:
    current_grade = float(input())
    class_counter += 1

    if current_grade < 4:
        fail_counter += 1
        if fail_counter == 2:
            print(f"{student_name} has been excluded at {class_counter} grade")
            break

        class_counter -= 1
    else:
        total_grades_sum += current_grade

    if class_counter == 12:
        average_grade = total_grades_sum / class_counter
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break

