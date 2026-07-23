# Student Management System V5

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Count Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(name, "added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for i, student in enumerate(students, start=1):
                print(i, ".", student)

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "found in the list.")
        else:
            print(name, "not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            students.remove(name)
            print(name, "deleted successfully!")
        else:
            print(name, "not found.")

    elif choice == "5":
        print("Total Students:", len(students))

    elif choice == "6":
        print("Thank you! Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
