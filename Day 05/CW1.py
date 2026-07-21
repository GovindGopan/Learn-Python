Python = {"Alice", "Bob", "Charlie", "David"}
print(Python)
Data_Science ={"Charlie", "David", "Emma", "Frank"}
print(Data_Science)

Python.add("Jake")
print("new student added to python : ",Python)
Data_Science.remove("Emma")
print("One student removed from data science: ", Data_Science)

print("students who are enrolled in both courses: ",Python.intersection(Data_Science))
print("Students enrolled only for python: ",Python.difference(Data_Science))
print("Combined list of students: ", Python.union(Data_Science))

Stud_count = {
    "Python" : len(Python),
    "Data_Science" : len(Data_Science),
}

for x,y in Stud_count.items():
    print(f"Course : {x} , No_of_students : {y}")


dict_comp = {x:y*2 for x,y in Stud_count.items()}
print(dict_comp)