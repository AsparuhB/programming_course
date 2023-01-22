width = int(input())
length = int(input())
heigth = int(input())

space = width * length * heigth

boxes_counter = 0

is_full = False

while True:
    command = input()
    if command == "Done":
        break

    if command != "Done":
        boxes = int(command)
        boxes_counter += boxes

    if boxes_counter > space:
        is_full = True
        break

diff = abs(space - boxes_counter)
if is_full:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")