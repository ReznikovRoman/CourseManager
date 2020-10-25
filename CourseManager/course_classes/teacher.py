from CourseManager.course_classes.person import Person


class Teacher(Person):
    """ Teacher, who teaches Course(s) and can evaluate Students' assignments """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary, teacher_id):
        super(Teacher, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__salary = salary
        self.__courses = []
        self.__id = teacher_id

    def get_salary(self):
        return self.__salary

    def get_courses(self):
        return self.__courses

    def add_course(self, course):
        self.__courses.append(course)

    def get_id(self):
        return self.__id

    def set_grade(self, enroll, grade):
        enroll.update_grade(grade)

        
        
        







