# Read input

steps_goal = 10000

steps_counter = 0
steps_reached = False

# Logic

while True:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        steps_counter += steps

    if steps_counter >= steps_goal:
        break

    if steps == "Going home":
        steps = int(input())
        steps_counter += steps
        break

if steps_counter >= steps_goal:
    steps_reached = True

diff = abs(steps_counter - steps_goal)

# Output

if steps_reached:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

