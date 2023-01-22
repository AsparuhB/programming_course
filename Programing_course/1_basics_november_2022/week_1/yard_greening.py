m2 = float(input())
#we enter the value of the square meters.
sum1 = float(m2 * 7.61)
#we print the sum of the square meters and the price needed for 1 sqrm
discount = 0.18 * sum1
#There is a discount of 18%, so we need to find this value also.
final_price = sum1 - discount
#The final price is the sum of the total sqrm + the price for 1sqrm minus the discount
print(f"The final price is: {final_price} lv")
print(f"The discount is: {discount} lv")
#We want to print the final price, but also the amount of the discount from it