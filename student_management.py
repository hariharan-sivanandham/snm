students = {}

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))

    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    students[student_id] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    print("Student added successfully")

def view_students():
    if not students:
        print("No students available")
        return

    for id, details in students.items():
        print("\nStudent ID:", id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Marks:", details["marks"])

def search_student():
    student_id = int(input("Enter Student ID to search: "))

    if student_id in students:
        s = students[student_id]
        print("\nName:", s["name"])
        print("Age:", s["age"])
        print("Marks:", s["marks"])
    else:
        print("Student not found")

def update_marks():
    student_id = int(input("Enter Student ID to update marks: "))

    if student_id in students:
        new_marks = []
        for i in range(3):
            mark = int(input(f"Enter new mark {i+1}: "))
            new_marks.append(mark)
        students[student_id]["marks"] = new_marks
        print("Marks updated successfully")
    else:
        print("Student not found")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    if student_id in students:
        del students[student_id]
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
