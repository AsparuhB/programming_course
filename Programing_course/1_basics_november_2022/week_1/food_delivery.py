#Restaurant has menus. We need to calculate the total for the menus

#menu prices
chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15
del_cost = 2.5
#the desert costs 20% of the total costs(witout delivery)
#The cost for delivery is 2.50, and will be added at the end
#Those are the prices for the menus in the restaurants


num_chicken = int(input())
num_fish = int(input())
num_veggie = int(input())
# Calculating menus costs, by multiplying the number of the menus * the cost for each menu
chicken = chicken_price * num_chicken
fish = fish_price * num_fish
veggie = veggie_price * num_veggie
# Calculating the total bill, by adding all the costs of the menus
total_cost = chicken + fish + veggie
#the desert costs 20% of the total costs(witout delivery)
desert = total_cost * 20 / 100

total = total_cost + desert + del_cost

print(f"{total}")


