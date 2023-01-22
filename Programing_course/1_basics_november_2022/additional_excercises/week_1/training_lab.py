#Read input

w_in_meters = float(input())
h_in_meters = float(input())

# Logic
w_in_cm = w_in_meters * 100
h_in_cm = h_in_meters * 100

w_of_desk = 120
h_of_desk = 70

hall = 100

desks_on_h = (h_in_cm - hall) // h_of_desk
desks_on_w = w_in_cm // w_of_desk

total = desks_on_w * desks_on_h - 3

#Output

print(f"{total:.0f}")


