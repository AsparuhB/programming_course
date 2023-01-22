# Read input

a = int(input())
b = int(input())
operator = input()  # +, -, *, /, %:

# Logic
# total = 0
#
# if b == 0:
#     print(f"Cannot divide {a} by zero")
# else:
#     if operator == "+":
#         total = a + b
#         if total % 2 == 0:
#             is_even = "even"
#         else:
#             is_even = "odd"
#         print(f"{a} {operator} {b} = {total} - {is_even}")
#     elif operator == "-":
#         total = a - b
#         if total % 2 == 0:
#             is_even = "even"
#         else:
#             is_even = "odd"
#         print(f"{a} {operator} {b} = {total} - {is_even}")
#     elif operator == "*":
#         total = a * b
#         if total % 2 == 0:
#             is_even = "even"
#         else:
#             is_even = "odd"
#         print(f"{a} {operator} {b} = {total} - {is_even}")
#     elif operator == "/":
#         total = a / b
#         print(f"{a} {operator} {b} = {total:.2f}")
#     elif operator == "%":
#         total = a % b
#         print(f"{a} {operator} {b} = {total}")
#

# Logic 2

total = 0
zero_flag = False

if operator == "+":
    total = a + b
elif operator == "-":
    total = a - b
elif operator == "*":
    total = a * b
elif operator == "/":
    if b == 0:
        zero_flag = True
    else:
        total = a / b
elif operator == "%":
    if b == 0:
        zero_flag = True
    else:
        total = a % b

# Output

if operator == "+" or operator == "-" or operator == "*":
    if total  % 2 == 0:
        print(f"{a} {operator} {b} = {total} - even")
    else:
        print(f"{a} {operator} {b} = {total} - odd")

elif operator == "/":
    if zero_flag:
        print(f"Cannot divide {a} by zero")
    else:
        print(f"{a} {operator} {b} = {total:.2f}")

elif operator == "%":
    if zero_flag:
        print(f"Cannot divide {a} by zero")
    else:
        print(f"{a} {operator} {b} = {total}")
