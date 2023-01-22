architect = input()
#We enter the persons name.
num_projects = int(input())
#we enter the number of project that is needed.
needed_hours = num_projects * 3
#we calculate the amount of projects and the time it takes to make ONE, so 3hrs to make one * number
print(f"The architect {architect} will need {needed_hours} hours to complete {num_projects} project/s.")
#we print with the f-string, because it's way easier to concatenate the string.