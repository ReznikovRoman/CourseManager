from course_classes.person import Person


class Teacher(Person):
    """ Teacher, who teaches Course(s) and can evaluate Students' assignments """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary):
        super(Teacher, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__salary = salary
        self.__courses = []

    def get_salary(self):
        return self.__salary

    def get_courses(self):
        return self.__courses

    def add_course(self, course):
        self.__courses.append(course)








