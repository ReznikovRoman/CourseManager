from CourseManager.course_classes.course import Course


class Enroll:
    """ Student's enrollment """
    def __init__(self, student, course: Course):
        self.__student = student
        self.__course = course
        self.__grades = []
        self.__has_certificate = False

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_grades(self):
        return self.__grades

    def update_grade(self, new_grade):
        self.__grades.append(new_grade)

    @property
    def final_grade(self):
        return float(sum(self.__grades) / len(self.__grades))

    def give_certificate(self):
        if self.final_grade >= self.__course.get_min_grade():
            self.__has_certificate = True
            new_certificate = f"Certificate in the course: {self.__course.get_name()}\n"
            self.__student.add_certificate(new_certificate)
        else:
            self.__has_certificate = False

    def get_certificate(self):
        return self.__has_certificate

    def unenroll(self, course):
        course.remove_enrollment(self)








