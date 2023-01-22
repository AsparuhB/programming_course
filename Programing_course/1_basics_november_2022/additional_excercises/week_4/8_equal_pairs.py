import sys

number_of_pairs = int(input())

pair_sum = 0
all_pair_sum = 0
previous_pair_sum = 0

maxdiff = -sys.maxsize

is_equal = False

for _ in range(number_of_pairs):
    first_digit = int(input())
    second_digit = int(input())

    pair_sum = first_digit + second_digit
    all_pair_sum += pair_sum

    maxdiff = abs(pair_sum - previous_pair_sum)


    previous_pair_sum = pair_sum


if all_pair_sum == number_of_pairs * pair_sum:
    print(f"Yes, value={pair_sum}")
else:
    print(f"No, maxdiff={maxdiff}")