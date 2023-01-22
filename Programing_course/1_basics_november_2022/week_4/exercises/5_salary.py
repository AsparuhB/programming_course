# Read input

open_tabs = int(input())
salary = int(input())

# Logic

innit_salary = salary

for tab in range(1, open_tabs + 1):
    current_tab = input()

    if current_tab == "Facebook":
        innit_salary -= 150
    elif current_tab == "Instagram":
        innit_salary -= 100
    elif current_tab == "Reddit":
        innit_salary -= 50

    if innit_salary <= 0:
        break

# Output

if innit_salary <= 0:
    print("You have lost your salary.")
else:
    print(innit_salary)

