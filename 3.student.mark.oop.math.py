import math
import numpy as np

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__gpa = 0.0

    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student DoB: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob} | GPA: {self.__gpa}/20")


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0

    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")
        self.__credits = int(input("Enter course credits: "))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
        
    def get_credits(self):
        return self.__credits

    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}")


class StudentMark:
    def __init__(self, student, course):
        self.__student = student
        self.__course = course
        self.__mark = 0.0

    def input(self):
        while True:
            mark_input = float(input(f"Enter mark for {self.__student.get_name()} (Course: {self.__course.get_name()} - Scale 20): "))
            if 0 <= mark_input <= 20:
                self.__mark = math.floor(mark_input * 10) / 10.0
                break
            else:
                print("Invalid mark! Please enter a value between 0 and 20.")

    def get_student_id(self):
        return self.__student.get_id()

    def get_course_credits(self):
        return self.__course.get_credits()

    def get_mark(self):
        return self.__mark

    def list(self):
        print(f"Student: {self.__student.get_name()} | Mark: {self.__mark}/20")


def calculate_gpa(student, marks_list):
    marks_array = []
    credits_array = []
    
    for sm in marks_list:
        if sm.get_student_id() == student.get_id():
            marks_array.append(sm.get_mark())
            credits_array.append(sm.get_course_credits())
            
    if len(marks_array) == 0:
        return 0.0
        
    np_marks = np.array(marks_array)
    np_credits = np.array(credits_array)
    
    gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
    return math.floor(gpa * 10) / 10.0


def sort_students_by_gpa(students_list):
    for i in range(len(students_list)):
        for j in range(i + 1, len(students_list)):
            if students_list[i].get_gpa() < students_list[j].get_gpa():
                temp = students_list[i]
                students_list[i] = students_list[j]
                students_list[j] = temp


if __name__ == "__main__":
    students = []
    courses = []
    marks = []

    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        s = Student()
        s.input()
        students.append(s)

    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        c = Course()
        c.input()
        courses.append(c)

    while True:
        print("\n1. Input marks")
        print("2. List students (Sorted by GPA)")
        print("3. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            c_id = input("Enter course ID: ")
            selected_course = None
            for c in courses:
                if c.get_id() == c_id:
                    selected_course = c
                    break
                    
            if selected_course:
                for s in students:
                    sm = StudentMark(s, selected_course)
                    sm.input()
                    marks.append(sm)
                    
                for s in students:
                    gpa = calculate_gpa(s, marks)
                    s.set_gpa(gpa)
            else:
                print("Course not found.")
                
        elif choice == '2':
            sort_students_by_gpa(students)
            print("\n--- STUDENTS ---")
            for s in students:
                s.list()
                
        elif choice == '3':
            break