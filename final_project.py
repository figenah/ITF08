import random

name = input("Name: ")
delivery_date = input("Delivery Date: ")

print(f"Name: {name}")
print(f"Delivery Date: {delivery_date}")


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1, 1000)
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1, 1000)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,
            "Student Number": self.student_number
        }

    def get_student_courses(self):
        if not self.courses_list:
            print("This student is not enrolled in any courses yet.")
        else:
            print("Courses enrolled:")
            for course in self.courses_list:
                print(f"Course Name: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        if not self.courses_list:
            print("This student is not enrolled in any courses yet.")
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)

students = []

while True:
    print("\nWelcome to the Student Management System")
    print("1. Add New Student")
    print("2. Delete Student")
    print("3. Display Student Details")
    print("4. Get Student Average Mark")
    print("5. Add Course to Student")
    print("6. Exit")

    selection = input("Enter your choice: ")

    if selection == "1":
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        student_age = int(input("Enter Student Age: "))

        student = Student(student_name, student_age, student_number)
        students.append(student)

        print("Student Added Successfully")
    elif selection == "2":
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break

        if found_student:
            students.remove(found_student)
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")
    elif selection == "3":
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break

        if found_student:
            student_details = found_student.get_student_details()
            print("\nStudent Details:")
            for key, value in student_details.items():
                print(f"{key}: {value}")
            found_student.get_student_courses()
        else:
            print("Student Not Found")
    elif selection == "4":
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break

        if found_student:
            average = found_student.get_student_average()
            if average > 0:
                print(f"\nStudent Average Mark: {average:.2f}")
        else:
            print("Student Not Found")
    elif selection == "5":
        student_number = input("Enter Student Number: ")
        found_student = None
        for student in students:
            if student.student_number == student_number:
                found_student = student
                break

        if found_student:
            course_name = input("Enter Course Name: ")
            course_mark = float(input("Enter Course Mark: "))
            found_student.enroll_course(course_name, course_mark)
            print("Course Added to Student Successfully")
        else:
            print("Student Not Found")
    elif selection == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
