number_of_inputs = int(input())

count_positives = []
sum_negatives = []

for _ in range(number_of_inputs):
    digit = int(input())

    if digit >= 0:
        count_positives.append(digit)
    else:
        sum_negatives.append(digit)

print(count_positives)
print(sum_negatives)
print(f"Count of positives: {len(count_positives)}")
print(f"Sum of negatives: {sum(sum_negatives)}")