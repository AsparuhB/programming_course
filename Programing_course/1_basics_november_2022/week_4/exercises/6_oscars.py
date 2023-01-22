# Read input

actor_name = input()
academy_points = float(input())
judges_number = int(input())

# Logic
total_points = academy_points
actor_points = 0


for judge in range(1, judges_number + 1):
    current_judge = input()
    current_judge_points = float(input())

    actor_points = ((len(current_judge) * current_judge_points) / 2)
    total_points = total_points + actor_points
    if total_points > 1250.5:
        break


if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")

else:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")