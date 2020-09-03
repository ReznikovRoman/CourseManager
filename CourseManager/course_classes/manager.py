
from CourseManager.course_classes.person import Person
from CourseManager.course_classes.course import Course


class Manager(Person):
    courses_lst = []
    """ Manager, who can create new Courses or change their names """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary):
        super(Manager, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__salary = salary
        self.__courses = []
        self.__permissions = "manager"

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def create_course(self, course_name, course_id):
        new_course = Course(course_name, course_id, self.__permissions)
        if new_course not in Manager.courses_lst:
            Manager.courses_lst.append(new_course)
        return new_course

    def change_course_name(self, course: Course, new_name):
        if course in self.__courses:
            course.change_name(new_name, self.__permissions)

    def change_course_min_grade(self, course: Course, new_grade):
        course.set_min_grade(new_grade, self.__permissions)

    def get_salary(self):
        return self.__salary

    def get_manager_courses(self):
        return self.__courses

    def get_permission(self):
        return self.__permissions

    def end_course(self, course):
        if course.get_state() != "closed":
            course.change_state(new_state="closed", permissions=self.__permissions)
            for enroll in course.get_enrollments():
                enroll.give_certificate()





