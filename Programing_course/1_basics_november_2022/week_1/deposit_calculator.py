#Make a program that calculates the total that you would get at the end of a deposit period at a cerain
#interest rate( in %). Use the formula down below

# total = depositet amount + time of the deposit(in months) * ((depositet amount * annual interest rate) / 12)

depositet_amount = float(input())
# We need to input the total deposit, that we will put in the bank
months = int(input())
# We need to input how many months this deposit will be in the bank
annual_interest_rate = float(input())
#the percentage entered is in %, but when you calculate it, should devide it by 100

total = depositet_amount + months * ((depositet_amount * annual_interest_rate / 100)/12)
# We need to find the total amount based on the formula given by the task
print(total)