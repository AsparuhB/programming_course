messages_sent = int(input())

for _ in range(messages_sent):
    command = int(input())

    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88:
        print("GREAT!")
    else:
        print("Bye.")
