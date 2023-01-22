lenght = int(input())
# We need the lenght of the aquarium in  cm
widht = int(input())
# we need the wight of the aquarium in cm
height = int(input())
# We need the height of the aquarium in cm
percent_acc = float(input())
#We need to calcute the percent of the volume of the accesoaries.

volume = lenght * widht * height
# Formula that we need to find the volume of the aquarium. Math formula
total_lt = volume / 1000
# Calculating the whole volume in lt, but our "volume" result is in cm, so we need to devide it by 1000, because
# 1lt = 1dm3, but 1dm = 10cm, so 1dm3 = 10cm * 10cm * 10cm, so 1dm3 = 1000cm3.
acc_volume = total_lt * (percent_acc / 100)

result = total_lt - acc_volume

print(result)