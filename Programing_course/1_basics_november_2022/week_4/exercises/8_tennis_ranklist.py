from math import floor
# Read Input

tournaments_num = int(input())
starting_points = int(input())

# Logic

total_points = starting_points
win_counter = 0
points_won = 0

for tournament in range(1, tournaments_num + 1):
    tournament_stage = input().lower()

    if tournament_stage == "w":
        win_counter += 1
        points_won += 2000
    elif tournament_stage == "f":
        points_won += 1200
    elif tournament_stage == "sf":
        points_won += 720

average_points = points_won / tournaments_num
total_points += points_won
percent_tournaments_won = win_counter / tournaments_num * 100

# Output

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_tournaments_won:.2f}%")

