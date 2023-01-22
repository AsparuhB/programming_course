#Rumen got an aquarium that is a paralelepiped. We have to enter the valus of the lenght, widht and the height
# We need to calculate how many litres of water are needed for the aquarium, if we know that the additional volume
#is taken by sand, trees, plants, heater and a pump.

lenght = int(input())
#lenght of the aquarium in cm
widht = int(input())
#widht of the aquarium in cm
height = int(input())
#height of the aquarium in cm
percent_taken = float(input())
#percent of the additional accesoaries in the aquarium that take up space.
#1lt = 1dm3

volume_in_cm = lenght * widht * height
#Calculating the volume in cm3, because the entered values are in cm
volume = volume_in_cm / 1000
#transfering the values from cm3 to lt, by deviding by 1000, because 1dm3 = 1tl = 1000cm3, so in order to find the

percent = (percent_taken * volume) / 100
#Calculating the percent value
total_volume = volume - percent
#calculating the total volume of water in lt, minus the percent of the additional accesoaries

print(f"{total_volume}")