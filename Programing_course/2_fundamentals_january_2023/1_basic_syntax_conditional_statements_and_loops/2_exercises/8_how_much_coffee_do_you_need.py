coffee_counter = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "coding":
        coffee_counter +=1
    elif command == "CODING":
        coffee_counter +=2
    elif command == "dog" or command == "cat":
        coffee_counter += 1
    elif command == "DOG" or command == "CAT":
        coffee_counter += 2
    elif command == "movie":
        coffee_counter += 1
    elif command == "MOVIE":
        coffee_counter += 2
    else:
        continue

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(f"{coffee_counter}")