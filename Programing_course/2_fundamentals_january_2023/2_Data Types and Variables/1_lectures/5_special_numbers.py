number = int(input())



for num in range(1, number + 1):
    sum_of_digits = 0
    digits = num
    is_true = False
    while digits > 0:
        sum_of_digits += digits % 10
        digits = digits // 10

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        is_true = True
        print(f"{num} -> {is_true}")
    else:
        print(f"{num} -> {is_true}")