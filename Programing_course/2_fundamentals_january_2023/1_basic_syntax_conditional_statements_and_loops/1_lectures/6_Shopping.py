budged = int(input())

total = budged

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        command = int(command)

        total -= command

    if total < 0:
        print("You went in overdraft!")
        break
