needed_book = input()
checked_books_counter = 0

is_found = True

while True:
    current_book = input()

    if current_book == needed_book:
        break

    if current_book == "No More Books":
        is_found = False
        break

    checked_books_counter += 1

if is_found:
    print(f"You checked {checked_books_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books_counter} books.")
