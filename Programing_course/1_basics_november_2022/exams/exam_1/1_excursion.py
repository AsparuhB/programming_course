number_friends = int(input())
number_nights = int(input())
number_transport_cards = int(input())
number_museum_tickets = int(input())

night_price = 20
transport_card_price = 1.60
museum_ticket = 6

price_for_nights = number_nights * night_price
price_for_cards = number_transport_cards * transport_card_price
price_for_museums = number_museum_tickets * museum_ticket

total_sum_for_one = price_for_nights + price_for_museums + price_for_cards

total_sum_for_all = total_sum_for_one * number_friends

total_sum_for_all = total_sum_for_all + (total_sum_for_all * 0.25)

print(f"{total_sum_for_all:.2f}")
