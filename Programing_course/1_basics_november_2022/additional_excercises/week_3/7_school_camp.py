# Read Input

season = input()
gender = input().lower()
num_students = int(input())
num_nights = int(input())

# Logic
sport = ""
stay = 0

if season == "Winter":
    if gender == "boys":
        sport = "Judo"
        stay += 9.60
    elif gender == "girls":
        sport = "Gymnastics"
        stay += 9.60
    elif gender == "mixed":
        sport = "Ski"
        stay = 10

elif season == "Spring":
    if gender == "boys":
        sport = "Tennis"
        stay += 7.20
    elif gender == "girls":
        sport = "Athletics"
        stay += 7.20
    elif gender == "mixed":
        sport = "Cycling"
        stay = 9.50
elif season == "Summer":
    if gender == "boys":
        sport = "Football"
        stay += 15
    elif gender == "girls":
        sport = "Volleyball"
        stay += 15
    elif gender == "mixed":
        sport = "Swimming"
        stay = 20

total = stay * num_nights * num_students

if num_students >= 50:
    total -= total * 0.50
elif 20 <= num_students < 50:
    total -= total * 0.15
elif 10 <= num_students < 20:
    total -= total * 0.05

print(f"{sport} {total:.2f} lv.")