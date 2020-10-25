
from CourseManager.course_classes.address import Address
from CourseManager.course_classes.course import Course
from CourseManager.course_classes.enroll import Enroll
from CourseManager.course_classes.person import Person
from CourseManager.course_classes.student import Student
from CourseManager.course_classes.teacher import Teacher
from CourseManager.course_classes.manager import Manager

import random
from datetime import date


# Managers sign up

# Manager - 1
manager_1_adr = Address(city="Cambridge", street="77 Massachusetts Avenue", zip="02139")
manager_1_date = date(1980, 7, 6)
manager_1 = Manager("Cari", "Angellotti", phone="(617) 258-7489", date_of_birth=manager_1_date,
                    address=manager_1_adr, salary=65000)

# Manager - 2
manager_2_adr = Address(city="Cambridge", street="77 Massachusetts Avenue", zip="02139")
manager_2_date = date(1985, 9, 17)
manager_2 = Manager("Kenneth", "Davies", phone="(617) 324-8188", date_of_birth=manager_2_date,
                    address=manager_2_adr, salary=75000)

# Get list of all managers
managers = [manager_1, manager_2]

# Create 3 Courses (Python, C++, JavaScript)

# Manager - 1 creates 2 courses (Python and C++)
python_course = manager_1.create_course("Python", 1)
c_course = manager_1.create_course("C++", 2)

# Manager - 2 creates 1 course (JavaScript)
javascript_course = manager_2.create_course("JavaScript", 3)

# Manager - 2 will also manage "Python Course"
manager_2.add_course(python_course)

# Get list of all Courses
curr_courses = Manager.courses_lst

#########################################################################################################

# Teachers sign up

# Teacher - 1
teacher_1_adr = Address(city="Berlin", street="Marchstrasse", zip="10587")
teacher_1_date = date(1975, 4, 23)
teacher_1 = Teacher("Rolf", "Niedermeier", phone="+49(0)30 314-21739", date_of_birth=teacher_1_date,
                    address=teacher_1_adr, salary=90000, teacher_id=1)

# Teacher - 2
teacher_2_adr = Address(city="Berlin", street="Bismarkstrasse", zip="10623")
teacher_2_date = date(1960, 8, 7)
teacher_2 = Teacher("Henning", "Meyer", phone="+49(0)30 314-21739", date_of_birth=teacher_2_date,
                    address=teacher_2_adr, salary=50000, teacher_id=2)

# Teacher - 3
teacher_3_adr = Address(city="Berlin", street="Straße des 17. Juni 135", zip="10623")
teacher_3_date = date(1975, 4, 23)
teacher_3 = Teacher("Ulf", "Schrader", phone="+49(0)30 314-73141", date_of_birth=teacher_3_date,
                    address=teacher_3_adr, salary=125000, teacher_id=3)

# Get list of all teachers
teachers = [teacher_1, teacher_2, teacher_3]

#########################################################################################################

# Teachers are selected for the course they will teach

# Teacher - 1
teacher_1.add_course(python_course)
teacher_1.add_course(javascript_course)

# Teacher - 2
teacher_2.add_course(c_course)

# Teacher - 3
teacher_3.add_course(python_course)
teacher_3.add_course(c_course)

# Python
python_course.add_teacher(teacher_1)
python_course.add_teacher(teacher_3)

# C++
c_course.add_teacher(teacher_2)
c_course.add_teacher(teacher_3)

# JavaScript
javascript_course.add_teacher(teacher_1)

#########################################################################################################

# Students sign up

# Student - 1
s1_date = date(2002, 3, 7)
s1_adr = Address(city="Moscow", street="Arbat Street")
s1 = Student("Roman", "Reznikov", "+7(985)111-11-11", s1_date, s1_adr, 1)

# Student - 2
s2_date = date(2000, 3, 25)
s2_adr = Address(city="Moscow", street="Kuznetsky Most")
s2 = Student("Andrey", "Andropov", "+7(985)111-11-11", s2_date, s2_adr, 2)

# Student - 3
s3_date = date(2002, 5, 1)
s3_adr = Address(city="Moscow", street="Petrovka Street")
s3 = Student("Philip", "Vorobyov", "+7(985)111-11-11", s3_date, s3_adr, 3)

# Student - 4
s4_date = date(2001, 6, 12)
s4_adr = Address(city="Moscow", street="Sadovnicheskaya Street")
s4 = Student("Nikolay", "Glukhov", "+7(985)111-11-11", s4_date, s4_adr, 4)

# Student - 5
s5_date = date(2002, 2, 28)
s5_adr = Address(city="Moscow", street="Tretyakovsky Proyezd")
s5 = Student("Anna", "Zhukova", "+7(985)111-11-11", s5_date, s5_adr, 5)

# Student - 6
s6_date = date(2000, 9, 30)
s6_adr = Address(city="St. Petersburg", street="Malaya Konyushennaya Ulitsa")
s6 = Student("Olga", "Ivanova", "+7(985)111-11-11", s6_date, s6_adr, 6)

# Student - 7
s7_date = date(2001, 12, 24)
s7_adr = Address(city="St. Petersburg", street="Ulitsa Zodchego Rossi")
s7 = Student("Vyacheslav", "Zimin", "+7(985)111-11-11", s7_date, s7_adr, 7)

# Student - 8
s8_date = date(2002, 4, 16)
s8_adr = Address(city="St. Petersburg", street="Malaya Sadovaya Ulitsa")
s8 = Student("Mikhail", "Kovalyov", "+7(985)111-11-11", s8_date, s8_adr, 8)

# Student - 9
s9_date = date(2000, 8, 9)
s9_adr = Address(city="St. Petersburg", street="Lesnoy Prospect")
s9 = Student("Maxim", "Solovyov", "+7(985)111-11-11", s9_date, s9_adr, 9)

# Get list of all Students
students = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

#####################################################################################################


print(
    """
    Welcome to the Course Manager!
    """
)

choice = ["-1"]


def has_permissions(manager: Manager, course_id: str):
    valid_ids = [str(i + 1) for i in range(len(manager.get_manager_courses()))]

    if manager.get_manager_courses():
        if course_id in valid_ids:
            return True
        else:
            return False


def main_menu():

    while choice[0] != "q":

        logged_ans = ("1", "2", "3")
        logged_as = input("Sign in as a (1-Manager; 2-Teacher; 3-Student): ")
        while logged_as not in logged_ans:
            logged_as = input("Sign in as a (1-Manager; 2-Teacher; 3-Student): ")
        print()

        if logged_as == "1":  # logged as a Manager
            manager_menu()
        elif logged_as == "2":  # logged as a Teacher
            teacher_menu()
        elif logged_as == "3":  # logged as a Student
            student_menu()

    input("\n\nPress 'Enter' to quit.")


def manager_menu():  # logged as a Manager

    # which Manager are you?
    print("Which Manager are you?")
    valid_ans = []
    for i in range(len(managers)):
        print(f"{i + 1}: {managers[i].get_full_name()}")
        valid_ans.append(str(i + 1))

    curr_manager_ind = input("Enter your ID: ")
    while curr_manager_ind not in valid_ans:
        curr_manager_ind = input("Enter your ID: ")
    curr_manager = managers[int(curr_manager_ind) - 1]

    while choice[0] != "0" and choice[0] != "q":

        print()
        print("What do you want to do?: ")
        print("1 - Create new Course\n"
              "2 - Get list of all Courses\n"
              "3 - Get list of Courses, which I can manage\n"
              "4 - Add Course to my list (will be able to Manage it)\n"
              "5 - Change the Course's name\n"
              "6 - Change the Course's min grade\n"
              "7 - End the Course\n"
              "8 - Add Student to the system\n"
              "0 - Quit back to the Main Menu\n"
              "q - Quit the 'Course Manager'\n")
        choice[0] = input("Enter your choice: ")
        print()

        if choice[0] == "1":  # create new Course
            print("Enter Course info")
            course_name = input("Course name: ")
            course_id = len(curr_courses) + 1
            new_course = curr_manager.create_course(course_name, course_id)
            print(f"{new_course} was created!", "\n")

        elif choice[0] == "2":  # get list of all Courses
            for c in Manager.courses_lst:
                print(c)
            print()

        elif choice[0] == "3":  # get list of all Manager's Courses
            if curr_manager.get_manager_courses():
                for c in curr_manager.get_manager_courses():
                    print(c)
                print()
            else:
                print("You do not manage any Course at the moment\n")

        elif choice[0] == "4":  # add Course, to be able to manage it
            print("Which course do you want to manage?")

            valid_ids = [str(i+1) for i in range(len(Manager.courses_lst))
                         if Manager.courses_lst[i] not in curr_manager.get_manager_courses()]

            for i in range(len(Manager.courses_lst)):
                if Manager.courses_lst[i] not in curr_manager.get_manager_courses():
                    print(f"{i+1} - {Manager.courses_lst[i]}")

            c_id = input("Enter your choice: ")
            while c_id not in valid_ids:
                c_id = input("Enter your choice: ")

            print()

            curr_manager.add_course(Manager.courses_lst[int(c_id) - 1])
            print(f"{Manager.courses_lst[int(c_id) - 1]} was added to your profile.")
            print()

        elif choice[0] == "5":  # change Course's name
            print("Which Course's name do you want to change?")

            if len(curr_manager.get_manager_courses()) > 0:
                for i in range(len(curr_manager.get_manager_courses())):
                    print(f"{i+1} - {curr_manager.get_manager_courses()[i]}")
                print()

                c_id = input("Enter your choice: ")
                while not has_permissions(curr_manager, c_id):
                    c_id = input("Enter your choice: ")

                print()

                new_name = input("Enter new Course's name: ")

                c = curr_manager.get_manager_courses()[int(c_id) - 1]
                curr_manager.change_course_name(c, new_name)

                print("Course name was changed!")
            else:
                print("You do not manage any Course at the moment.")

        elif choice[0] == "6":  # change Course's min grade (this grade or higher in order to get a certificate)
            print("Which Course's grade do you want to change?")

            if len(curr_manager.get_manager_courses()) > 0:
                for i in range(len(curr_manager.get_manager_courses())):
                    print(f"{i + 1} - {curr_manager.get_manager_courses()[i]}")
                print()

                c_id = input("Enter your choice: ")
                while not has_permissions(curr_manager, c_id):
                    c_id = input("Enter your choice: ")

                print()

                c = curr_manager.get_manager_courses()[int(c_id) - 1]

                print(f"Current minimum grade: {c.get_min_grade()}")

                while True:
                    try:
                        new_grade = float(input("Enter new grade: "))
                        break
                    except ValueError as e:
                        print("Please, enter new grade as a number (can be with the floating point)")

                c = curr_manager.get_manager_courses()[int(c_id) - 1]
                curr_manager.change_course_min_grade(c, new_grade)
            else:
                print("You do not manage any Course at the moment.")

        elif choice[0] == "7":  # end Course
            print("Which Course's grade do you want to end?")
            if len(curr_manager.get_manager_courses()) > 0:
                for i in range(len(curr_manager.get_manager_courses())):
                    print(f"{i + 1} - {curr_manager.get_manager_courses()[i]}")
                print()

                c_id = input("Enter your choice: ")
                while not has_permissions(curr_manager, c_id):
                    c_id = input("Enter your choice: ")

                print()

                c = curr_manager.get_manager_courses()[int(c_id) - 1]
                curr_manager.end_course(c)

                print(f"Course {c.get_name()} has been ended.")
            else:
                print("You do not manage any Course at the moment.")

        elif choice[0] == "8":  # add new student to the student's list
            # get student's info
            print("Enter info about the Student")
            s_f_name = input("Enter student's first name: ")
            s_l_name = input("Enter student's last name: ")
            s_phone = input("Enter student's phone: ")
            print("Enter Student's date of birth")
            s_year = int(input("Enter year of birth: "))
            s_month = int(input("Enter month of birth: "))
            s_day = int(input("Enter day of birth: "))
            s_date_of_birth = date(s_year, s_month, s_day)
            s_address = input("Enter student's address: ")

            # create new student and add him to the list
            new_student = Student(s_f_name, s_l_name, s_phone, s_date_of_birth, s_address, len(students) + 1)
            students.append(new_student)
            print("Student was added to the list, student's ID: ", new_student.get_id())

        elif choice[0] == "9":  # add new teacher to the teacher's list
            # get teacher's info
            print("Enter info about the Teacher")
            t_f_name = input("Enter teacher's first name: ")
            t_l_name = input("Enter teacher's last name: ")
            t_phone = input("Enter teacher's phone: ")
            print("Enter Teacher's date of birth")
            t_year = int(input("Enter year of birth: "))
            t_month = int(input("Enter month of birth: "))
            t_day = int(input("Enter day of birth: "))
            t_date_of_birth = date(t_year, t_month, t_day)
            t_address = input("Enter teacher's address: ")
            t_salary = int(input("Enter teacher's salary"))

            # create new teacher and add him to the list
            new_teacher = Teacher(t_f_name, t_l_name, t_phone, t_date_of_birth, t_address, t_salary, len(teachers) + 1)
            teachers.append(new_teacher)
            print("Teacher was added to the list, teacher's ID: ", new_teacher.get_id())

        elif choice[0] == "0":  # go back to the main menu
            choice[0] = "-1"
            break

        elif choice[0] == "q":  # quit the program
            break

        else:
            print()
            print(f"There is no command: {choice[0]}")
            print("What do you want to do?: ")
            print("1 - Create new Course\n"
                  "2 - Get list of all Courses\n"
                  "3 - Get list of Courses, which I can manage\n"
                  "4 - Add Course to my list (will be able to Manage it)\n"
                  "5 - Change the Course's name\n"
                  "6 - Change the Course's min grade\n"
                  "7 - End the Course\n"
                  "8 - Add Student to the system\n"
                  "9 - Add Teacher to the system\n"
                  "0 - Quit back to the Main Menu\n"
                  "q - Quit the 'Course Manager'\n")
            choice[0] = input("Enter your choice: ")


def teacher_menu():  # logged as a Teacher

    # get list of all Courses
    # choose a Course, where you want to teach
    # evaluate  Student in the Course

    # What's your Teacher's ID?
    print("Enter your Teacher's ID")

    while True:
        try:
            curr_teacher_id = int(input("Enter your ID: "))
            if curr_teacher_id in [t.get_id() for t in teachers]:
                curr_teacher = teachers[curr_teacher_id - 1]
                print(f"Welcome back, {curr_teacher.get_full_name()}!")
                break
            else:
                print("There is no teacher with id: ", curr_teacher_id)
        except ValueError as e:
            print("Please, enter your Teacher ID as a number.")

    while choice[0] != "0" and choice[0] != "q":

        print()
        print("What do you want to do?: ")
        print("1 - Get list of all available courses\n"
              "2 - Choose a new Course to teach\n"
              "3 - Get list of all courses, where I am teaching\n"
              "4 - Evaluate students in the course\n"
              "5 - Get the list of students from the Course\n"
              "0 - Quit back to the Main Menu\n"
              "q - Quit the 'Course Manager'\n")
        choice[0] = input("Enter your choice: ")
        print()

        if choice[0] == "1":  # get list of all courses
            for course in Manager.courses_lst:
                print(course)

        elif choice[0] == "2":  # choose a Course, where you want to teach
            print("In which course do you want to teach?")
            # print all courses, where teacher is not teaching for now
            teacher_courses = [course for course in curr_teacher.get_courses()]
            available_courses = [course for course in Manager.courses_lst if course not in teacher_courses]
            for course_ind in range(len(available_courses)):
                print(f"{course_ind + 1} - {available_courses[course_ind]}")

            while True:
                try:
                    chosen_course_ind = int(input("Enter course index: "))
                    if chosen_course_ind in [i + 1 for i in range(len(available_courses))]:
                        chosen_course = available_courses[chosen_course_ind - 1]
                        break
                    else:
                        print("Please, enter the correct course index.")
                except ValueError as e:
                    print("Please, enter course index as a digit.")

            chosen_course.add_teacher(curr_teacher)
            curr_teacher.add_course(chosen_course)
            print("You were successfully assigned to the ", chosen_course, "\n")

        elif choice[0] == "3":  # get list of all courses, where the current teachers is teaching
            if len(curr_teacher.get_courses()) != 0:
                for course in curr_teacher.get_courses():
                    print(course)
            else:
                print("You are not assigned to any course.")

        elif choice[0] == "4":  # add new grade to the student
            teacher_courses = curr_teacher.get_courses()
            if len(teacher_courses) > 0:
                print("In which course do you want to evaluate students?")

                for course_ind in range(len(teacher_courses)):
                    print(f"{course_ind + 1} - {teacher_courses[course_ind]}")

                while True:
                    try:
                        chosen_course_id = int(input("Enter course index: "))
                        if chosen_course_id in [i + 1 for i in range(len(teacher_courses))]:
                            chosen_course = teacher_courses[chosen_course_id - 1]
                            break
                        else:
                            print("Please, enter correct course index.")
                    except ValueError as e:
                        print("Please, enter course index as a digit.")

                if len(chosen_course.get_enrollments()) > 0:

                    print("\nAdd new mark for each student (0-100):")
                    for enroll in chosen_course.get_enrollments():
                        while True:
                            try:
                                curr_mark = int(input(f"{enroll.get_student().get_full_name()} - "))
                                if 0 <= curr_mark <= 100:
                                    break
                                else:
                                    print("Please, enter mark (0-100)")
                            except ValueError as e:
                                print("Please, enter mark as a digit.")

                        enroll.update_grade(curr_mark)

                    print("All marks were added.")
                else:
                    print("There are currently no students in this course.")
            else:
                print("You are not assigned to any course.")

        elif choice[0] == "5":  # get the list of students from the course
            # print all courses, where teacher is not teaching for now
            teacher_courses = [course for course in curr_teacher.get_courses()]

            if len(teacher_courses) > 0:
                print("Students from which course do you want to see?")
                for course_ind in range(len(teacher_courses)):
                    print(f"{course_ind + 1} - {teacher_courses[course_ind]}")

                while True:
                    try:
                        chosen_course_ind = int(input("Enter course index: "))
                        if chosen_course_ind in [i + 1 for i in range(len(teacher_courses))]:
                            chosen_course = teacher_courses[chosen_course_ind - 1]
                            break
                        else:
                            print("Please, enter the correct course index.")
                    except ValueError as e:
                        print("Please, enter course index as a digit.")

                if len(chosen_course.get_enrollments()) > 0:
                    for i in range(len(chosen_course.get_enrollments())):
                        print(f"{i+1} - {chosen_course.get_enrollments()[i].get_student().get_full_name()}")
                else:
                    print("There are currently no students in the course ", chosen_course.get_name())
            else:
                print("You are not assigned to any course.")

        elif choice[0] == "0":  # go back to the main menu
            choice[0] = "-1"
            break

        elif choice[0] == "q":  # quit the program
            break

        else:
            print()
            print(f"There is no command: {choice[0]}")
            print("What do you want to do?: ")
            print("1 - Get list of all available courses\n"
                  "2 - Choose a new Course to teach\n"
                  "3 - Get list of all courses, where I am teaching\n"
                  "4 - Evaluate students in the course\n"
                  "5 - Get the list of students from the Course\n"
                  "0 - Quit back to the Main Menu\n"
                  "q - Quit the 'Course Manager'\n")
            choice[0] = input("Enter your choice: ")


def student_menu():  # logged as a Student

    # What's your Student's ID?
    print("Enter your Student's ID")

    while True:
        try:
            curr_student_id = int(input("Enter your ID: "))
            if curr_student_id in [s.get_id() for s in students]:
                curr_student = students[curr_student_id - 1]
                break
            else:
                print("There is no student with id: ", curr_student_id)

        except ValueError as e:
            print("Please, enter your Student ID as a number.")

    while choice[0] != "0" and choice[0] != "q":

        print()
        print("What do you want to do?: ")
        print("1 - Get list of all available courses\n"
              "2 - Enroll in new Course\n"
              "3 - Get list of Courses, in which I am enrolled\n"
              "4 - Get list of my marks from the Course\n"
              "5 - Get list of all certificates from Courses\n"
              "6 - Unenroll from the course\n"
              "0 - Quit back to the Main Menu\n"
              "q - Quit the 'Course Manager'\n")
        choice[0] = input("Enter your choice: ")
        print()

        if choice[0] == "1":  # get list of all courses
            for course in Manager.courses_lst:
                print(course)

        elif choice[0] == "2":  # enroll in the new course
            print("In which course do you want to enroll?")
            # print all courses, in which student is not enrolled
            student_courses = [enroll.get_course() for enroll in curr_student.get_enrolls()]
            available_courses = [course for course in Manager.courses_lst if course not in student_courses]
            for course_ind in range(len(available_courses)):
                print(f"{course_ind + 1} - {available_courses[course_ind]}")

            while True:
                try:
                    chosen_course_ind = int(input("Enter course index: "))
                    if chosen_course_ind in [i+1 for i in range(len(available_courses))]:
                        chosen_course = available_courses[chosen_course_ind - 1]
                        break
                    else:
                        print("Please, enter the correct course index.")
                except ValueError as e:
                    print("Please, enter course index as a digit.")

            new_enroll = Enroll(curr_student, chosen_course)
            chosen_course.add_enrollment(new_enroll)
            curr_student.add_enroll(new_enroll)
            print("You were successfully enrolled in the ", chosen_course, "\n")

        elif choice[0] == "3":  # get list of all courses in which student is enrolled
            if len(curr_student.get_enrolls()) > 0:
                for enroll in curr_student.get_enrolls():
                    print(enroll.get_course())
            else:
                print("You are not enrolled in any course.")

        elif choice[0] == "4":  # get list of marks from the Course
            student_courses = [enroll.get_course() for enroll in curr_student.get_enrolls()]

            if len(curr_student.get_enrolls()) > 0:
                print("Marks from which course do you want to see?")

                for course_ind in range(len(student_courses)):
                    print(f"{course_ind + 1} - {student_courses[course_ind]}")

                while True:
                    try:
                        chosen_course_id = int(input("Enter course index: "))
                        if chosen_course_id in [i + 1 for i in range(len(student_courses))]:
                            chosen_course = student_courses[chosen_course_id - 1]
                            break
                        else:
                            print("Please, enter correct course index.")
                    except ValueError as e:
                        print("Please, enter course index as a digit.")

                for enroll in curr_student.get_enrolls():
                    if enroll.get_course() is chosen_course:
                        curr_enroll = enroll

                if curr_enroll.get_grades():
                    print("\nYour marks: ", *curr_enroll.get_grades())
                else:
                    print("\nYou don't have any marks in the course ", chosen_course.get_name())
            else:
                print("You are not enrolled in any course.")

        elif choice[0] == "5":  # get list of all certificates
            student_courses = [enroll.get_course() for enroll in curr_student.get_enrolls()]

            if len(curr_student.get_certificates()) > 0:
               curr_student.print_certificates()
            else:
                print("\nYou don't have any certificates.")

        elif choice[0] == "6":  # unenroll from the course
            student_courses = [enroll.get_course() for enroll in curr_student.get_enrolls()]

            if len(curr_student.get_enrolls()) > 0:
                print("From which course do you want to unenroll?")

                while True:
                    try:
                        chosen_course_id = int(input("Enter course index: "))
                        if chosen_course_id in [i + 1 for i in range(len(student_courses))]:
                            removable_course = student_courses[chosen_course_id - 1]
                            break
                        else:
                            print("Please, enter correct course index.")
                    except ValueError as e:
                        print("Please, enter course index as a digit.")

                for enroll in curr_student.get_enrolls():
                    if enroll.get_course() is removable_course:
                        enroll_to_remove = enroll

                curr_student.unenroll(enroll_to_remove)
                removable_course.remove_enrollment(enroll_to_remove)
                print("You was successfully unenrolled from the ", removable_course.get_name())

                for course_ind in range(len(student_courses)):
                    print(f"{course_ind + 1} - {student_courses[course_ind]}")
            else:
                print("You are not enrolled in any course.")

        elif choice[0] == "0":  # go back to the main menu
            choice[0] = "-1"
            break

        elif choice[0] == "q":  # quit the program
            break

        else:
            print()
            print(f"There is no command: {choice[0]}")
            print("What do you want to do?: ")
            print("1 - Get list of all available courses\n"
                  "2 - Enroll in new Course\n"
                  "3 - Get list of Courses, in which I am enrolled\n"
                  "4 - Get list of my marks from the Course\n"
                  "5 - Get list of all certificates from Courses\n"
                  "6 - Unenroll from the course\n"
                  "0 - Quit back to the Main Menu\n"
                  "q - Quit the 'Course Manager'\n")
            choice[0] = input("Enter your choice: ")


if __name__ == '__main__':
    main_menu()


#########################################################################################################

# Students choose, in which course they want to enroll (python_course, c_course, javascript_course)

'''

enroll_11 = Enroll(s1, python_course)
python_course.add_enrollment(enroll_11)
s1.add_enroll(enroll_11)
enroll_12 = Enroll(s1, c_course)
c_course.add_enrollment(enroll_12)
s1.add_enroll(enroll_12)

enroll_21 = Enroll(s1, python_course)
python_course.add_enrollment(enroll_21)
s2.add_enroll(enroll_21)

enroll_31 = Enroll(s3, python_course)
python_course.add_enrollment(enroll_31)
s3.add_enroll(enroll_31)

enroll_41 = Enroll(s4, c_course)
python_course.add_enrollment(enroll_41)
s4.add_enroll(enroll_41)

enroll_51 = Enroll(s5, javascript_course)
python_course.add_enrollment(enroll_51)
s5.add_enroll(enroll_51)

enroll_61 = Enroll(s6, javascript_course)
python_course.add_enrollment(enroll_61)
s6.add_enroll(enroll_61)

enroll_71 = Enroll(s7, c_course)
python_course.add_enrollment(enroll_71)
s7.add_enroll(enroll_71)

enroll_81 = Enroll(s8, c_course)
python_course.add_enrollment(enroll_81)
s8.add_enroll(enroll_81)

enroll_91 = Enroll(s9, javascript_course)
python_course.add_enrollment(enroll_91)
s9.add_enroll(enroll_91)

#########################################################################################################

# Teachers update students' marks


def update_grade(a_courses):
    for a_course in a_courses:
        for enroll in a_course.get_enrollments():
            enroll.update_grade(random.randrange(2, 6))


t1_courses = teacher_1.get_courses()
t2_courses = teacher_2.get_courses()
t3_courses = teacher_3.get_courses()

update_grade(t1_courses)
update_grade(t2_courses)
update_grade(t3_courses)

#########################################################################################################

# All courses are finished and students can get their certificates


def end_course(a_course: Course):
    for enroll in a_course.get_enrollments():
        enroll.give_certificate()
    print(f"Course {a_course.get_name()} ({a_course.get_code()}) is finished.")


for course in curr_courses:
    end_course(course)

print()

#########################################################################################################

# Get students, who has certificate

for s in students:
    for s_enroll in s.get_enrolls():
        if s_enroll.get_certificate():
            print(s.get_full_name(), "has a", s_enroll.print_certificate())


#########################################################################################################
'''



