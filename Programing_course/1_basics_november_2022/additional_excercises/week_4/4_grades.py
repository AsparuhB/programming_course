total_students = int(input())

top_student_counter = 0
between_4_5_counter = 0
between_3_4_counter = 0
fail_counter = 0

grade_counter = 0

for _ in range(total_students):
    student_grade = float(input())

    grade_counter += student_grade

    if student_grade < 3:
        fail_counter += 1
    elif 3 <= student_grade < 4:
        between_3_4_counter += 1
    elif 4 <= student_grade < 5:
        between_4_5_counter += 1
    elif student_grade >= 5:
        top_student_counter += 1

top_percent = top_student_counter / total_students * 100
four_to_five_percent = between_4_5_counter / total_students * 100
three_to_four_percent = between_3_4_counter / total_students * 100
fail_percent = fail_counter / total_students * 100

average_grade = grade_counter / total_students

print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {four_to_five_percent:.2f}%")
print(f"Between 3.00 and 3.99: {three_to_four_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")