student_grades = {}


def add_student(name, grade):
    student_grades[name] = grade
    print(f"{name} scored a {grade}")


def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been removed")

    else:
        print(f"{name} not found!")


def displaystudents():

    print("Student List")
    for name, grade in student_grades.items():
        print(f"student: {name} - grade: {grade}")


def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} new grade is {grade}")


add_student("mlee", 45)
add_student("abigail", 95)

update_grade("mlee", 100)


def find_grade(name):
    if name in student_grades:
        print(f"Student found. Grade: {student_grades[name]}")
    else:
        print(f"Student not found")


def average_grade():
    grades = []
    for name, grade in student_grades.items():
        grades.append(grade)
    if grades:
        num_students = len(grades)
        average = sum(grades) / num_students
        print(f"average: {average}")
    else:
        print("no student grades found")


displaystudents()

find_grade("mlee")

find_grade("abigail")

average_grade()
