while True:
    word = ""
    command = input()

    if command == "SoftUni":
        continue

    if command == "End":
        break
    else:
        for char in command:
            word += 2 * char
    print(word)