number_floors = int(input())
number_rooms = int(input())

for floor in range(number_floors, 0, -1):
    for room in range(number_rooms):
        if floor == number_floors:
            print(f"L{floor}{room}", end=" ")
        else:
            if floor % 2 == 0:
                print(f"O{floor}{room}", end=" ")
            else:
                print(f"A{floor}{room}", end=" ")
    print()