# number_of_ints = int(input())
#
# list_even = []
# list_odd = []
# list_negative = []
# list_positive = []
#
#
# for digit in range(number_of_ints):
#     current_number = int(input())
#
#     if current_number >= 0:
#         list_positive.append(current_number)
#         if current_number % 2 == 0:
#             list_even.append(current_number)
#         else:
#             list_odd.append(current_number)
#     elif current_number < 0:
#         list_negative.append(current_number)
#         if current_number % 2 == 0:
#             list_even.append(current_number)
#         else:
#             list_odd.append(current_number)
#
#
# command = input()
#
# if command == "even":
#     print(list_even)
# elif command == "odd":
#     print(list_odd)
# elif command == "negative":
#     print(list_negative)
# elif command == "positive":
#     print(list_positive)

number_of_lines = int(input())

# constant values
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

#accepting number from user input
numbers = []

for _ in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []

# number_filtering
for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)