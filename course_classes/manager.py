
from course_classes.person import Person
from course_classes.course import Course


class Manager(Person):
    courses_lst = []
    """ Manager, who can create new Courses or change their names """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary):
        super(Manager, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self._salary = salary
        self._courses = []
        self._permissions = "manager"

    def add_course(self, course):
        if course not in self._courses:
            self._courses.append(course)

    def create_course(self, course_name, course_id):
        new_course = Course(course_name, course_id, self._permissions)
        if new_course not in Manager.courses_lst:
            Manager.courses_lst.append(new_course)
        self.add_course(new_course)
        return new_course

    def change_course_name(self, course: Course, new_name):
        course.change_name(new_name, self._permissions)

    def get_salary(self):
        return self._salary

    def get_manager_courses(self):
        return self._courses

    def get_permission(self):
        return self._permissions





