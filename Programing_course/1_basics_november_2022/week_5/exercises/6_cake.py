cake_width = int(input())
cake_length = int(input())

cake_total = cake_length * cake_width
cake_piece_counter = 0

cake_is_over = False

while True:
    current_piece = input()

    if current_piece != "STOP":
        current_piece = int(current_piece)
        cake_piece_counter += current_piece

    if current_piece == "STOP":
        break

    if cake_piece_counter >= cake_total:
        break

if cake_piece_counter >= cake_total:
    cake_is_over = True


diff = abs(cake_total - cake_piece_counter)

if cake_is_over:
    print(f'No more cake left! You need {diff} pieces more.')
else:
    print(f"{diff} pieces are left.")