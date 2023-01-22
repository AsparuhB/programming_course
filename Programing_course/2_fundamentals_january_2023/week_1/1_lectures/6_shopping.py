budged = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        exit()
    else:
        product_price = int(command)

        budged -= product_price
        if budged < 0:
            print("You went in overdraft!")
            break