class Student:
    all_students = []

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def show_details(self):
        print("\nStudent Details:")
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Marks  : {self.marks}")

    @classmethod
    def find_student_by_rollno(cls, rollno):
        for student in cls.all_students:
            if student.rollno == rollno:
                return student
        return None

    @classmethod
    def add_student(cls):
        name = input("Enter Your Name: ")
        rollno = int(input("Enter Your Roll No: "))
        marks = int(input("Enter Your Marks: "))

        student = cls(name, rollno, marks)
        cls.all_students.append(student)

        print(f"Student {name} added successfully!")

    @classmethod
    def update_student_marks(cls):
        rollno = int(input("Enter Roll No: "))
        student = cls.find_student_by_rollno(rollno)

        if student:
            new_marks = int(input("Enter New Marks: "))
            student.update_marks(new_marks)
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found!")
            return

        for student in cls.all_students:
            student.show_details()


def menu():
    while True:
        print("\n=========== Student APP ===========")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            Student.add_student()
        elif choice == 2:
            Student.update_student_marks()
        elif choice == 3:
            Student.show_all_students()
        elif choice == 4:
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    menu()