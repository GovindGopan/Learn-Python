info = """A Python course offers an interactive introduction to coding using 
one of the world's most versatile and beginner-friendly programming languages."""

print("Length of information: ",(len(info)))

print("First character : ", info[0])

print("Last character : ", info[-1])

print("First 50 characters : ", info[0:51])

info_replace = info.replace("Python","PYTHON")
info_lower = info.lower()
info_strip = info.strip()
info_split = info.split()
words = len(info_split)
check_for_course = "course" in info
print("The word course is present in the informmation : ", check_for_course)

print("The course description is {} characters long and has {} words.".format(len(info), words))



