number_of_string = int(input())

for _ in range(number_of_string):
    string_input = input()
    string_pure = True

    for ch in string_input:

        if ch == "," or ch == "." or ch == "_":
            string_pure = False

    if string_pure:
        print(f"{string_input} is pure.")
    else:
        print(f"{string_input} is not pure!")
