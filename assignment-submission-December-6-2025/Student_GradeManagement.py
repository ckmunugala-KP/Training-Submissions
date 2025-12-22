class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Must be between 0 and 100.")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        print("\n------ Student Information ------")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Grades     : {self.grades}")
        print(f"Average    : {self.calculate_average():.2f}")
        print("---------------------------------")


students = {}  # dictionary to store students by student_id


def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    student = Student(name, student_id)
    students[student_id] = student

    print("Enter grades for the student (type 'done' to finish):")
    while True:
        grade_input = input("Grade: ")

        if grade_input.lower() == "done":
            break

        try:
            grade = float(grade_input)
            student.add_grade(grade)
        except ValueError:
            print("Invalid input. Enter a number.")


def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        students[student_id].display_info()
    else:
        print("No student found with that ID!")


# ---------------- MAIN MENU ----------------

while True:
    print("\n===== Student Grade Management System =====")
    print("1. Add New Student")
    print("2. Search Existing Student")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        print("Exiting Program. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
