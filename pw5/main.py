import numpy as np
import math
from domains import StudentMark
import input as ui_input
import output as ui_output

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


def sort_students(students_list):
    for i in range(len(students_list)):
        for j in range(i + 1, len(students_list)):
            if students_list[i].get_gpa() < students_list[j].get_gpa():
                temp = students_list[i]
                students_list[i] = students_list[j]
                students_list[j] = temp

import os
import zipfile

def load_data():
    if os.path.exists("students.dat"):
        print("Decompressing students.dat...")
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()

def save_and_compress_data(students, courses, marks):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")
            
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")
            
    with open("marks.txt", "w") as f:
        for mark in marks:
            f.write(f"{mark.course_id},{mark.student_id},{mark.value}\n")

    print("Compressing data into students.dat...")
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("students.txt")
        zipf.write("courses.txt")
        zipf.write("marks.txt")

if __name__ == "__main__":
    load_data()
    students = []
    courses = []
    marks = []

    ui_input.input_all_students(students)
    ui_input.input_all_courses(courses)

    while True:
        print("\n1. Input marks")
        print("2. Show sorted students")
        print("3. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            ui_output.print_courses(courses)
            c_id = input("Enter course ID to input marks: ")
            
            selected_c = None
            for c in courses:
                if c.get_id() == c_id:
                    selected_c = c
                    break
                    
            if selected_c:
                for s in students:
                    sm = StudentMark(s, selected_c)
                    sm.input()
                    marks.append(sm)
                    
                for s in students:
                    gpa = calculate_gpa(s, marks)
                    s.set_gpa(gpa)
            else:
                print("Course not found!")
                
        elif choice == '2':
            sort_students(students)
            ui_output.print_students(students)
            
        elif choice == '3':
            save_and_compress_data(students, courses, marks)
            break

        