# We need a program to calculate the expenses for painting the kitchen and living room

pr_nylon = 1.5
#The nylons price for a m2
pr_paint = 14.50
#The price of the paint, per litre
pr_thinner = 5
#The price for the paint thinner, per litre.

#Just in case Rumen wants to add an additional 10% paint volume and 2 m2 of nylon and of course 0.40 for bags
bag = 0.40

#The money he has to pay to the handy man is 30% of the total of all expenses for materials.

n_nylon = int(input())
#The number of nylon m2 needed
n_paint = int(input())
#the litres of paint needed
n_thinner = int(input())
#the litres of thinner needed

hour = int(input())
#the hours needed to complete the painting of the kitchen and living room

#We need to print the result in a f-string

nylon = n_nylon * pr_nylon
# the cost of the nylon
paint = n_paint * pr_paint
# the cost of the paint
thinner = n_thinner * pr_thinner
# the total cost of the thinner
add_paint = paint * 10 / 100
# the additional paint that the guy needs
total_paint = paint + add_paint
# the cost of the additional paint
add_nylon = 2
add_nylon_cost = add_nylon * pr_nylon
#He wants to have 2 additional m2 of nylon
total_for_materials = total_paint + nylon + thinner + add_nylon_cost + bag
# calculating the total cost for the materials
hour_cost = total_for_materials * 30 / 100
# the hour cost is 30% of the total cost for the materials
total_for_hours = hour * hour_cost
# the total cost for the hours neede
total_for_everything = total_for_materials + total_for_hours
#Total for everything is the total cost for the materials + the cost for the hours
print(f"{total_for_everything}")

