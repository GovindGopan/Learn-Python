import os

try:
    if os.path.exists("students.txt"):
        f = open("students.txt", "r")
        print("Existing names:")
        print(f.read())
        f.close()

    no_of_stud = int(input("Enter number of students to add: "))

    f = open("students.txt", "a")

    for i in range(no_of_stud):
        name = input("Enter student name: ")
        f.write(name + "\n")

    f.close()

    f = open("students.txt", "r")
    print("\nUpdated list:")
    print(f.read())

finally:
    f.close()