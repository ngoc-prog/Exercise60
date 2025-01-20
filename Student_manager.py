from Student import Student
from datetime import datetime


class StudentManager:
    def __init__(self):
        self.students = []

    # Add a student to the list
    def add_student(self, student):
        self.students.append(student)

    # Calculate the total number of students
    def total_students(self):
        return len(self.students)

    # Find students by full name
    def find_by_full_name(self, name):
        return [student for student in self.students if student.full_name.lower() == name.lower()]

    # Find students with birthdays in the current month
    def find_birthdays_in_current_month(self):
        current_month = datetime.now().month
        return [student for student in self.students if student.date_of_birth.month == current_month]

    # Sort students by age in ascending order
    def sort_by_age(self):
        self.students.sort(key=lambda student: student.age)

    # Print all students
    def print_all_students(self):
        for student in self.students:
            print(student.print_info())

