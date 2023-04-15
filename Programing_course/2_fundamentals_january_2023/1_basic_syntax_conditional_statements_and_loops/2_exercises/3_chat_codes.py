num_commands = int(input())

for num in range(0, num_commands):
    command = int(input())

    if command == 88:
        print("Hello")

    elif command == 86:
        print("How are you?")

    elif command < 88 and command != 86:
        print("GREAT!")

    else:
        print("Bye.")