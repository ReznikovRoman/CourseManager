
from course_classes.address import Address
from course_classes.course import Course
from course_classes.enroll import Enroll
from course_classes.person import Person
from course_classes.student import Student
from course_classes.teacher import Teacher

from datetime import date
import random


# Create 3 Courses (Python, C++, JavaScript)
python_course = Course(name="Python", code="001")
c_course = Course(name="C++", code="002")
javascript_course = Course(name="JavaScript", code="003")

#########################################################################################################

# Teachers sign up

# Teacher - 1
teacher_1_adr = Address(city="Berlin", street="Marchstrasse", zip=10587)
teacher_1_date = date(1975, 4, 23)
teacher_1 = Teacher("Rolf", "Niedermeier", phone="+49(0)30 314-21739", date_of_birth=teacher_1_date,
                    address=teacher_1_adr, salary=90000)

# Teacher - 2
teacher_2_adr = Address(city="Berlin", street="Bismarkstrasse", zip=10623)
teacher_2_date = date(1960, 8, 7)
teacher_2 = Teacher("Henning", "Meyer", phone="+49(0)30 314-21739", date_of_birth=teacher_2_date,
                    address=teacher_2_adr, salary=50000)

# Teacher - 3
teacher_3_adr = Address(city="Berlin", street="Straße des 17. Juni 135", zip=10623)
teacher_3_date = date(1975, 4, 23)
teacher_3 = Teacher("Ulf", "Schrader", phone="+49(0)30 314-73141", date_of_birth=teacher_3_date,
                    address=teacher_3_adr, salary=125000)

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

#########################################################################################################

# Students choose, in which course they want to enroll (python_course, c_course, javascript_course)


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
        if enroll.get_final_grade() > 4:
            enroll.update_certificate(a_has_certificate=True)
        else:
            enroll.update_certificate(a_has_certificate=False)
    print(f"Course {a_course.get_name()} ({a_course.get_code()}) is finished.")


curr_courses = [python_course, c_course, javascript_course]

for course in curr_courses:
    end_course(course)

print()

#########################################################################################################

# Get students, who has certificate

curr_students = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

for s in curr_students:
    for s_enroll in s.get_enrolls():
        if s_enroll.get_certificate():
            print(s.get_full_name(), "has a", s_enroll.print_certificate())


#########################################################################################################






