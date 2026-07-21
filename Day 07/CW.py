Grocery_List  = ["milk" , "bread" ,"eggs"]
item =0 
def add_item(item):
     Grocery_List.append(item)

def remove_last_item():
     Grocery_List.pop()
    
x = lambda y : print("Item : ",y)
for z in Grocery_List:
    x(z)
    
remove_last_item()
add_item("meat")

print("list after change :",Grocery_List)

def count_characters(item):  
         if  len(item) == 0:
            return 0
         else :
            return len(item[0]) + count_characters(item[1:])
    
    
print("Sum of characters of all items: ", count_characters(Grocery_List))      
       
       
    

    
    
    