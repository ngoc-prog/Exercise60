from datetime import datetime


class Student:
    def __init__(self, student_id, full_name, date_of_birth):
        self.student_id = student_id
        self.full_name = full_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")  # Expect format "YYYY-MM-DD"

    # Read-only property for last name
    @property
    def last_name(self):
        return self.full_name.split()[-1]

    # Read-only property for first name
    @property
    def first_name(self):
        return self.full_name.split()[0]

    # Read-only property for age
    @property
    def age(self):
        today = datetime.now()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    # Method to print student information
    def print_info(self):
        return f"ID: {self.student_id}, Full Name: {self.full_name}, DOB: {self.date_of_birth.strftime('%Y-%m-%d')}, Age: {self.age}"

