Web_Development = ["Alice", "Bob", "Charlie"] 
Data_Science = ["David", "Eve", "Frank"]
UI_UX_Design = ["Grace", "Henry", "Ivy"]

all_participants = [Web_Development, Data_Science, UI_UX_Design]

Web_Development.append("Jack")
Data_Science.insert(2, "Kathy")
UI_UX_Design.pop()

Data_Science_new = list(Data_Science)  
Data_Science.clear() 

print(Web_Development[0:3])

list_comp = [len(participant) for participant in Data_Science_new]
print(list_comp)

if "Asha" in all_participants :
    print("Asha is a participant i n the program")
    
else:
    print("Asha is not a participant in the program")

tuple = (Web_Development[0], Data_Science_new[0], UI_UX_Design[0])
print(tuple)
