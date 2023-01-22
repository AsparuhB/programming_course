examiners = int(input())

all_grades_average = 0
presentation_counter = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    current_grade_counter = 0
    presentation_counter += 1

    for grade in range(examiners):
        current_grade = float(input())
        current_grade_counter += current_grade
        all_grades_average += current_grade

    average_grade = current_grade_counter / examiners
    print(f"{presentation} - {average_grade:.2f}.")

all_time_average = all_grades_average / (examiners * presentation_counter)
print(f"Student's final assessment is {all_time_average:.2f}.")