# Read input

x = float(input())
y = float(input())
h = float(input())

# Logic

# Green paint - 1l for 3.4m2
house_front = x * x - (1.2 * 2)
house_back = x * x
house_sides = 2 * (y * x - 1.5 * 1.5)
house_in_m2 = (house_front + house_sides + house_back)
green_paint_in_liters = house_in_m2 / 3.4

#Red paint - 1l = 4.3m2

roof_in_m2= (2 * x * h / 2) + (2 * x * y)
red_paint_in_liters = roof_in_m2 / 4.3

#Output

print(f"{green_paint_in_liters:.2f}")
print(f"{red_paint_in_liters:.2f}")
