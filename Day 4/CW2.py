#list named color
#tuple named flowers
#iterate in both
#slice and create sublist/ sub tuple
#each list item and display length

color = ["Red", "Green", "Blue", "Yellow", "Purple"]
flower = ("Rose", "Tulip", "Lily", "Daisy", "Sunflower")

for i in color:
    print(i)
    
print("\n")
for j in flower:
    print(j)

color_sublist = color[1:3]
flower_subtuple = flower[1:3]

print("\nColor sublist: ",color_sublist)
print("Flower subtuple: ",flower_subtuple)

print("\nColors: ")
for item in color: 
    print(item,"-",len(item))
    
print("\nFlowers: ")
for item in flower:
    print(item,"-",len(item))





