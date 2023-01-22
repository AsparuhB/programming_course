# Read Input

choice = input().lower()

# Logic // Output

if choice == "banana" or choice == "apple" or choice == "kiwi" or choice == "cherry" \
    or choice == "lemon" or choice == "grapes":
    print("fruit")
elif choice == "tomato" or choice == "cucumber" or choice == "pepper" or choice == "carrot":
    print("vegetable")
else:
    print("unknown")
