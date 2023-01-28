number_of_strings = int(input())
keyword = input()

list_of_strings = []
list_with_keyword = []

for _ in range(number_of_strings):
    current_string = input()

    list_of_strings.append(current_string)
    if keyword in current_string:
        list_with_keyword.append(current_string)

print(list_of_strings)
print(list_with_keyword)
