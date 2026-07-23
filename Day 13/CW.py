import os

item = input("Enter the name of a new item: ")

if os.path.exists("items.txt"):
    f = open("items.txt", "a")
    f.write("\n" + item)
    f.close()

else:
    f = open("items.txt", "x")
    f.write(item)
    f.close()

f = open("items.txt", "r")
print(f.read())
f.close()