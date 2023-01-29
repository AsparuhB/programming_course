import math

people_using_elevator = int(input())
elevator_capacity = int(input())

courses = math.ceil(people_using_elevator / elevator_capacity)

print(courses)
