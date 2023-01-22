bad_grades = int(input())
tasks_completed = 0
bad_grades_counter = 0
grades_total = 0

had_enough = False

while True:
    current_task = input()

    if current_task == "Enough":
        had_enough = True
        average_score = grades_total / tasks_completed
        break

    last_problem = current_task
    current_grade = int(input())

    tasks_completed += 1
    grades_total += current_grade

    if current_grade <= 4:
        bad_grades_counter += 1

    if bad_grades_counter == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break

if had_enough:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {tasks_completed}")
    print(f"Last problem: {last_problem}")