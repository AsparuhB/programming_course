handouts = input().split(", ")
number_of_beggars = int(input())
final_sums = []
starting_index = 0
handouts_as_digit = []

for idx in handouts:
    handouts_as_digit.append(int(idx))

while starting_index < number_of_beggars:
    current_beggar_sum = 0

    for current_index in range(starting_index, len(handouts_as_digit), number_of_beggars):
        current_beggar_sum += handouts_as_digit[current_index]
    final_sums.append(current_beggar_sum)
    starting_index += 1

print(final_sums)
