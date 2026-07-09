fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "cabbage", "cauliflower"]
beverages = ["water", "juice", "soda"]

fruits.append("guava")
vegetables.insert(2,"cucumber")
beverages.pop()

#nested list
inventory = [fruits, vegetables, beverages]

print(fruits[0:3])


len_of_fruits = [len(item) for item in fruits]                
print(len_of_fruits)              

if "water" in beverages :
    print("water is available in beverages")

#tuple containing first item of each list
tuple =(fruits[0], vegetables[0], beverages[0])

