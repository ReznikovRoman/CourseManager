
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
python_course = manager_1.create_course("Python", "001")
c_course = manager_1.create_course("C++", "002")

# Manager - 2 creates 1 course (JavaScript)
javascript_course = manager_2.create_course("JavaScript", "003")

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
                    address=teacher_1_adr, salary=90000)

# Teacher - 2
teacher_2_adr = Address(city="Berlin", street="Bismarkstrasse", zip="10623")
teacher_2_date = date(1960, 8, 7)
teacher_2 = Teacher("Henning", "Meyer", phone="+49(0)30 314-21739", date_of_birth=teacher_2_date,
                    address=teacher_2_adr, salary=50000)

# Teacher - 3
teacher_3_adr = Address(city="Berlin", street="Straße des 17. Juni 135", zip="10623")
teacher_3_date = date(1975, 4, 23)
teacher_3 = Teacher("Ulf", "Schrader", phone="+49(0)30 314-73141", date_of_birth=teacher_3_date,
                    address=teacher_3_adr, salary=125000)

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
s1 = Student("Roman", "Reznikov", "+7(985)111-11-11", s1_date, s1_adr)

# Student - 2
s2_date = date(2000, 3, 25)
s2_adr = Address(city="Moscow", street="Kuznetsky Most")
s2 = Student("Andrey", "Andropov", "+7(985)111-11-11", s2_date, s2_adr)

# Student - 3
s3_date = date(2002, 5, 1)
s3_adr = Address(city="Moscow", street="Petrovka Street")
s3 = Student("Philip", "Vorobyov", "+7(985)111-11-11", s3_date, s3_adr)

# Student - 4
s4_date = date(2001, 6, 12)
s4_adr = Address(city="Moscow", street="Sadovnicheskaya Street")
s4 = Student("Nikolay", "Glukhov", "+7(985)111-11-11", s4_date, s4_adr)

# Student - 5
s5_date = date(2002, 2, 28)
s5_adr = Address(city="Moscow", street="Tretyakovsky Proyezd")
s5 = Student("Anna", "Zhukova", "+7(985)111-11-11", s5_date, s5_adr)

# Student - 6
s6_date = date(2000, 9, 30)
s6_adr = Address(city="St. Petersburg", street="Malaya Konyushennaya Ulitsa")
s6 = Student("Olga", "Ivanova", "+7(985)111-11-11", s6_date, s6_adr)

# Student - 7
s7_date = date(2001, 12, 24)
s7_adr = Address(city="St. Petersburg", street="Ulitsa Zodchego Rossi")
s7 = Student("Vyacheslav", "Zimin", "+7(985)111-11-11", s7_date, s7_adr)

# Student - 8
s8_date = date(2002, 4, 16)
s8_adr = Address(city="St. Petersburg", street="Malaya Sadovaya Ulitsa")
s8 = Student("Mikhail", "Kovalyov", "+7(985)111-11-11", s8_date, s8_adr)

# Student - 9
s9_date = date(2000, 8, 9)
s9_adr = Address(city="St. Petersburg", street="Lesnoy Prospect")
s9 = Student("Maxim", "Solovyov", "+7(985)111-11-11", s9_date, s9_adr)

# Get list of all Students
students = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

#####################################################################################################


print(
    """
    Welcome to the Course Manager!
    """
)

choice = ["-1"]


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
              "4 - Add Course to your list (you will be able to Manage it)\n"
              "5 - Change the Course's name\n"
              "6 - Change the Course's min grade\n"
              "7 - End the Course\n"
              "0 - Quit back to the Main Menu\n"
              "q - Quit the 'Course Manager'\n")
        choice[0] = input("Enter your choice: ")
        print()

        if choice[0] == "1":  # create new Course
            print("Enter Course info")
            course_name = input("Course name: ")
            course_id = input("Course ID: ")
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

            valid_ids = [str(i + 1) for i in range(len(curr_manager.get_manager_courses()))]

            if curr_manager.get_manager_courses():
                for i in range(len(curr_manager.get_manager_courses())):
                    print(f"{i+1} - {curr_manager.get_manager_courses()[i]}")
                print()

            c_id = input("Enter your choice: ")
            while c_id not in valid_ids:
                c_id = input("Enter your choice: ")

            print()

            new_name = input("Enter new Course's name: ")

            c = curr_manager.get_manager_courses()[int(c_id) - 1]
            curr_manager.change_course_name(c, new_name)

            print("Course name was changed!")

        elif choice[0] == "6":  # change Course's min grade, which Student must have in order to get a certificate
            pass

        elif choice[0] == "7":  # end Course
            pass

        elif choice[0] == "0":  # go back to the main menu
            choice[0] = "-1"
            break

        elif choice[0] == "q":  # quit the program
            break

        else:
            print()
            print(f"There is no command {choice[0]}")
            print("What do you want to do?: ")
            print("1 - Create new Course\n"
                  "2 - Get list of all Courses\n"
                  "3 - Add Course to your list (you will be able to Manage it)\n"
                  "4 - Change the Course's name\n"
                  "5 - Change the Course's min grade\n"
                  "6 - End the Course\n"
                  "0 - Quit back to the Main Menu\n"
                  "q - Quit the 'Course Manager'\n")
            choice[0] = input("Enter your choice: ")


def teacher_menu():  # logged as a Teacher
    pass
    # get list of all Courses
    # choose a Course, where you want to teach
    # evaluate  Student in the Course


def student_menu():  # logged as a Student
    pass
    # get list of all Courses
    # enroll in the Course
    # get list of all marks from the Course
    # get all certificates, if any


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



