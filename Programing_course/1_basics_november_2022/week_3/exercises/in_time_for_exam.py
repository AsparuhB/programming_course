# Read Input

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

# Logic

exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minutes

time = abs(arrival_time - exam_time)

time_hour = time // 60
time_minutes = time % 60

#Output

if arrival_time == exam_time:
    print("On time")

else:
    if exam_time < arrival_time:
        if time >= 60:
            print("Late")
            print(f"{time_hour}:{time_minutes:02d} hours after the start")
        else:
            print("Late")
            print(f"{time_minutes} minutes after the start")
    if exam_time > arrival_time:
        if time >= 60:
            print("Early")
            print(f"{time_hour}:{time_minutes:02d} hours before the start")
        elif time <= 30:
            print("On time")
            print(f"{time_minutes} minutes before the start")
        elif time > 30:
            print("Early")
            print(f"{time_minutes} minutes before the start")