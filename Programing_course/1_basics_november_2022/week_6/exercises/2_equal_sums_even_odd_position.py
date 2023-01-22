starting_num = int(input())
ending_num = int(input())

for number in range(starting_num, ending_num + 1):
    str_number = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    # for index in range(0, len(str_number)):
    #     digit = int(str_number[index])
    #     if index % 2 == 0:
    #         even_sum += digit
    #     else:
    #         odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=" ")
