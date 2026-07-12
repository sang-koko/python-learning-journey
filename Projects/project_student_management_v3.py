while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
        name = input("Enter Student Name: ")
        usn = input("Enter Student USN: ")
        branch = input("Enter Branch: ")
        marks = int(input("Enter Marks: "))
 print("\n----- Student Details -----")
        print("Name   :", name)
        print("USN    :", usn)
        print("Branch :", branch)
        print("Marks  :", marks)
if marks >= 35:
            print("Result : Pass")
        else:
            print("Result : Fail")
 elif choice == 2:
        print("Thank you! Exiting Program...")
        break
else:
        print("Invalid Choice!")
