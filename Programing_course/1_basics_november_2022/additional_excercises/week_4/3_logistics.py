freight_number = int(input())

bus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

bus_price = 0
truck_price = 0
train_price = 0

total_load_tonnage = 0

for freight in range(1, freight_number + 1):
    tonnage = int(input())

    if tonnage <= 3:
        bus_tonnage += tonnage
        bus_price += tonnage * 200
        total_load_tonnage += tonnage
    if 4 <= tonnage <= 11:
        truck_tonnage += tonnage
        truck_price += tonnage * 175
        total_load_tonnage += tonnage
    if tonnage >= 12:
        train_tonnage += tonnage
        train_price += tonnage * 120
        total_load_tonnage += tonnage

average_price_percentage = (bus_price + truck_price + train_price) / total_load_tonnage

average_bus_loads_percentage = bus_tonnage / total_load_tonnage * 100
average_truck_loads_percentage = truck_tonnage / total_load_tonnage * 100
average_train_loads_percentage = train_tonnage / total_load_tonnage * 100

print(f'{average_price_percentage:.2f}')
print(f"{average_bus_loads_percentage:.2f}%")
print(f"{average_truck_loads_percentage:.2f}%")
print(f"{average_train_loads_percentage:.2f}%")