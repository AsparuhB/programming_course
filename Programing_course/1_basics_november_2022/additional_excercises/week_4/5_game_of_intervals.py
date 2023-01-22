game_duration = int(input())

game_result = 0
zero_nine_counter = 0
ten_nineteen_counter = 0
twenty_twentynite_counter = 0
thirty_thirtynine_counter = 0
fourty_fifty_counter = 0
invalid_numbers_counter = 0

for _ in range(game_duration):
    game_points = int(input())

    if (0 > game_points) or (game_points > 50):
        invalid_numbers_counter += 1
        game_result = game_result / 2


    if 0 <= game_points < 10:
        game_result += game_points * 0.20
        zero_nine_counter += 1
    elif 10 <= game_points < 20:
        game_result += game_points * 0.30
        ten_nineteen_counter += 1
    elif 20 <= game_points < 30:
        game_result += game_points * 0.40
        twenty_twentynite_counter += 1
    elif 30 <= game_points < 40:
        game_result += 50
        thirty_thirtynine_counter += 1
    elif 40 <= game_points <= 50:
        game_result += 100
        fourty_fifty_counter += 1

zero_nine_percent = zero_nine_counter / game_duration * 100
ten_nineteen_percent = ten_nineteen_counter / game_duration * 100
twenty_twentynite_percent = twenty_twentynite_counter / game_duration * 100
thirty_thirtynine_percent = thirty_thirtynine_counter / game_duration * 100
fourty_fifty_percent = fourty_fifty_counter / game_duration * 100
invalid_numbers_percent = invalid_numbers_counter / game_duration * 100


print(f"{game_result:.2f}")
print(f"From 0 to 9: {zero_nine_percent:.2f}%")
print(f"From 10 to 19: {ten_nineteen_percent:.2f}%")
print(f"From 20 to 29: {twenty_twentynite_percent:.2f}%")
print(f"From 30 to 39: {thirty_thirtynine_percent:.2f}%")
print(f"From 40 to 50: {fourty_fifty_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")