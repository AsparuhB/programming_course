# Read Input

degrease = float(input())

#Logic

if 5 <= degrease < 12:
    print("Cold")
elif 12 <= degrease < 15:
    print("Cool")
elif 15 <= degrease <= 20:
    print("Mild")
elif 20 < degrease < 26:
    print("Warm")
elif 26 <= degrease <= 35:
    print("Hot")
else:
    print("unknown")

