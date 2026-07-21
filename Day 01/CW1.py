import random
apple_juice  = 15.5
orange_juice = 20
grape_juice  = 10.25

total_volume = apple_juice + orange_juice + grape_juice
print("Total volume: ",total_volume)

total_volume = int(total_volume)
print("Total volume (integer): ",total_volume)

total_volume = str(total_volume)
print("Total volume (string): ",total_volume)

print("Additional bonus litres: ", random.randrange(5,10)) 