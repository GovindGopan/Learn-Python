Frontend = {"Alice", "Bob", "Charlie", "David"}
Backend = {"Charlie", "David", "Emma", "Frank"}

Backend.add("Jake")
Frontend.remove("Alice")

print("Students enrolled in both courses:",Frontend.intersection(Backend))
print("Students who are enrolled only in Backend, but not in Frontend:",Backend.difference(Frontend))
print("Total number of unique students:", len(Frontend.union(Backend)))

Course_info = {
    "Frontend" : len(Frontend),
    "Backend" : len(Backend),
}

for x,y in Course_info.items():
    print(f"Course : {x} , No_of_students : {y}")
    
new_course_info = {k: v for k, v in Course_info.items()}
new_course_info["Fullstack"] = len(Frontend) + len(Backend)

print(new_course_info)
