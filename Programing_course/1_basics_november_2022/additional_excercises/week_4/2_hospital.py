calculation_interval = int(input())

doctors = 7
day = 1

patients_treated = 0
patients_untreated = 0

for days in range(1, calculation_interval + 1):
    if day % 3 == 0 and patients_untreated > patients_treated: doctors += 1

    patients_to_be_checked = int(input())

    if doctors >= patients_to_be_checked:
        patients_treated += patients_to_be_checked
    else:
        doctors < patients_to_be_checked
        patients_treated += doctors
        patients_untreated += patients_to_be_checked - doctors
    day += 1

print(f"Treated patients: {patients_treated}.")
print(f"Untreated patients: {patients_untreated}.")
