
from course_classes.person import Person


class Teacher(Person):
    """ Teacher, who teaches Course(s) and can evaluate Students' assignments """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary):
        super(Teacher, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self._salary = salary
        self._courses = []

    def get_salary(self):
        return self._salary

    def get_courses(self):
        return self._courses

    def add_course(self, course):
        self._courses.append(course)








