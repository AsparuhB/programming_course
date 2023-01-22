# Read Input

off_days_num = int(input())

# Logic

working_days = 365 - off_days_num

work_play_time = working_days * 63
off_play_time = off_days_num * 127

total_play_time = work_play_time + off_play_time

play_norm = 30000
diff = abs(play_norm - total_play_time)
hours = diff // 60
minutes = diff % 60

# Output

if play_norm >= total_play_time:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")