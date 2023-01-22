sum_to_be_gathered = int(input())

item_turn = 0
sum_gathered = 0
cs_sum = 0
cc_sum = 0
cs_counter = 0
cc_counter = 0

is_gathered = False

while True:


    items_sum = input()

    if items_sum == "End":
        print("Failed to collect required money for charity.")
        break

    items_sum = int(items_sum)
    if sum_gathered >= sum_to_be_gathered:
        is_gathered = True

        break
    item_turn += 1

    if item_turn % 2 == 0:
        if items_sum < 10:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
            sum_gathered += items_sum
            cc_counter += 1
            cc_sum += items_sum
    else:
        if items_sum > 100:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
            sum_gathered += items_sum
            cs_counter += 1
            cs_sum += items_sum

    if sum_gathered >= sum_to_be_gathered:
        cs_average = cs_sum / cs_counter
        cc_average = cc_sum / cc_counter
        print(f"Average CS: {cs_average:.2f}")
        print(f"Average CC: {cc_average:.2f}")
        break