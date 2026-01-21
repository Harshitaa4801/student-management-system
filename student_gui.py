students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append({"roll": roll, "name": name, "course": course})
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("⚠ No student records found.")
        return
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Course: {s['course']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("❌ Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("🗑 Student deleted.")
            return
    print("❌ Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("👋 Exiting program.")
        break
    else:
        print("⚠ Invalid choice")