students = {}

while True:
    print("\n----- STUDENT RESULT MANAGER -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully!")

    # View Students
    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"{name} : {marks}")
        else:
            print("No student records found.")

    # Check Result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            marks = students[name]

            if marks >= 40:
                print(f"{name} passed with {marks} marks")
            else:
                print(f"{name} failed with {marks} marks")
        else:
            print("Student not found.")

    # Delete Student
    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print(f"{name} deleted successfully!")
        else:
            print("Student not found.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
