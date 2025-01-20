from Student_manager import StudentManager
from Student import Student


def input_student():
    """Input student details from the user"""
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    return Student(student_id, full_name, date_of_birth)


def menu():
    manager = StudentManager()

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Find Student by Full Name")
        print("4. Find Students with Birthdays in Current Month")
        print("5. Sort Students by Age")
        print("6. Total Number of Students")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student = input_student()
            manager.add_student(student)
            print("Student added successfully.")

        elif choice == "2":
            if not manager.students:
                print("No students available.")
            else:
                print("\n--- Student List ---")
                manager.print_all_students()

        elif choice == "3":
            name = input("Enter full name to search: ")
            results = manager.find_by_full_name(name)
            if results:
                print("\n--- Search Results ---")
                for student in results:
                    print(student.print_info())
            else:
                print("No student found with that name.")

        elif choice == "4":
            results = manager.find_birthdays_in_current_month()
            if results:
                print("\n--- Students with Birthdays this Month ---")
                for student in results:
                    print(student.print_info())
            else:
                print("No students have birthdays this month.")

        elif choice == "5":
            manager.sort_by_age()
            print("Students sorted by age in ascending order.")

        elif choice == "6":
            print(f"Total number of students: {manager.total_students()}")

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
