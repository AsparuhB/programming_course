# Annie needs to get supplies for school. She has to get packs of pens, packs of markers and detergent for
# the black board. Annie is frequently in the shop, so he gets a discount. We need a program to calculate
# how much money Annie has to gather in order to buy all the stuff

packet_of_pens = 5.80
# The price for a packet of pens
packet_of_markers = 7.20
# The price of markers of markets
detergent = 1.20
# price of the detergent for 1 liter

num_pens = int(input())
# The number of packets ot pens
num_markers = int(input())
# The number of packets of markers
detergent_lt = int(input())
# the liters of the detergent needed.
percentage = int(input())

total = (num_pens * packet_of_pens) + (num_markers * packet_of_markers) + (detergent_lt * detergent)
# Find the total, which is the number of packages times the price needed for one packages
total_percentage = total * percentage / 100
# Calculate the total percentage by multiplying the total sum times the percentage discount
# ( the percentage needs to be divided by 100 in order to convert it to %)

total_minus_percentage = total - total_percentage
# Finding the total sum that needs to be paid minus the percentage of the discount
print(total_minus_percentage)

