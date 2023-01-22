
coffee_counter = 0

while True:
    input_line = input()
    if input_line == "END":
        break

    if input_line == "coding" or input_line == "cat" or input_line == "dog" or input_line == "movie":
        coffee_counter += 1

    if input_line == "CODING" or input_line == "CAT" or input_line == "DOG" or input_line == "MOVIE":
        coffee_counter += 2

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(f"{coffee_counter}")
    