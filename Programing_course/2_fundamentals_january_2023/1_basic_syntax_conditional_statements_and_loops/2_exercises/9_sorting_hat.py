while True:
    command = input()

    char_lenght = 0

    if command == "Welcome!":
        break

    if command == "Voldemort":
        print("You must not speak of that name!")
        exit()

    for char in command:
        char_lenght += 1

    if char_lenght < 5:
        print(f"{command} goes to Gryffindor.")
    elif char_lenght == 5:
        print(f"{command} goes to Slytherin.")
    elif char_lenght == 6:
        print(f"{command} goes to Ravenclaw.")
    elif char_lenght > 6:
        print(f"{command} goes to Hufflepuff.")

print("Welcome to Hogwarts.")