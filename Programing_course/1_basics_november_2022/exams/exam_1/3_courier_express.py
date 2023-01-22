parcel_weight = float(input())
shipping_type = input().lower()
distance_in_km = int(input())

total = 0

if shipping_type == "standard":
    if parcel_weight < 1:
        total += distance_in_km * 0.03
    elif parcel_weight < 10:
        total += distance_in_km * 0.05
    elif parcel_weight < 40:
        total += distance_in_km * 0.1
    elif parcel_weight < 90:
        total += distance_in_km * 0.15
    elif parcel_weight < 150:
        total += distance_in_km * 0.20

if shipping_type == "express":
    if parcel_weight < 1:
        total += distance_in_km * 0.03
        overprice = parcel_weight * (total * 0.80)
        total += overprice
    elif parcel_weight < 10:
        total += distance_in_km * 0.05
        overprice = parcel_weight * (total * 0.40)
        total += overprice
    elif parcel_weight < 40:
        total += distance_in_km * 0.10
        overprice = parcel_weight * (total * 0.05)
        total += overprice
    elif parcel_weight < 90:
        total += distance_in_km * 0.15
        overprice = parcel_weight * (total * 0.02)
        total += overprice
    elif parcel_weight < 150:
        total += distance_in_km * 0.20
        overprice = parcel_weight * (total * 0.01)
        total += overprice


print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {total:.2f} lv.")
