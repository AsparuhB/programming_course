name = input()
#we input the name of the person
surname = input()
#we input the surname of the person
age = int(input())
#We have to write int before the input, because the years should be a whole number
town = input()
#We input the name of the town.

#All inputs are strings, so we have to assign data type, if we need something else (int, float, boolean)

print(f"You are {name} {surname}, a {age}-years old person from {town}.")
#We can concatenata text with the f-string.