# Student Management System V4
# Using Functions

students = []


def add_student():
    name = input("Enter Student Name: ")
    students.append(name)
    print("✅ Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("❌ No students found.")
    else:
        print("\n===== Student List =====")
        for i in range(len(students)):
            print(i + 1, ".", students[i])


def search_student():
    name = input("Enter Student Name to Search: ")

    if name in students:
        print("✅ Student Found!")
    else:
        print("❌ Student Not Found.")


def delete_student():
    name = input("Enter Student Name to Delete: ")

    if name in students:
        students.remove(name)
        print("✅ Student Deleted Successfully!")
    else:
        print("❌ Student Not Found.")


def count_students():
    print("Total Students =", len(students))


def menu():
    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM V4 ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Count Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            count_students()

        elif choice == "6":
            print("Thank You! Exiting Program...")
            break

        else:
            print("❌ Invalid Choice! Please try again.")


# Start the program
menu()
