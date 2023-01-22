from math import pi

area = input()


if area == "square":
    a = float(input())
    print(f"{a * a:.3f}")
elif area == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif area == "circle":
    r = float(input())
    print(f"{pi * r ** 2:.3f}")
elif area == "triangle":
    a = float(input())
    ha = float(input())
    print(f"{a * ha / 2:.3f}")