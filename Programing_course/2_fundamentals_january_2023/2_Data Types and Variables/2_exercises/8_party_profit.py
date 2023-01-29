import math
group_size = int(input()) # group to start seeking gold and glory
days = int(input()) #days searched

total_coins = 0 # Gold accumulated

companions = group_size # faithful companions lol

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2

    if day % 15 == 0:
        companions += 5

    total_coins += 50 # Initial coins got
    total_coins -= 2 * companions # coins spent on food

    if day % 3 == 0:
        total_coins -= 3 * companions # party with water

    if day % 5 == 0:
        total_coins += 20 * companions # additional gold for slaying a big monster
        if day % 5 == 0 and day % 3 == 0:
            total_coins -= 2 * companions # additional feast

average_coins = total_coins // companions

print(f"{companions} companions received {math.floor(average_coins)} coins each.")

