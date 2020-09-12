from CourseManager.course_classes.course import Course


class Enroll:
    """ Student's enrollment """
    def __init__(self, student, course: Course):
        self.__student = student
        self.__course = course
        self.__grade = 0
        self.__grade_count = 0
        self.__has_certificate = False

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_grade(self):
        return self.__grade

    def get_grade_count(self):
        return self.__grade_count

    def update_grade(self, new_grade):
        self.__grade += new_grade
        self.__grade_count += 1

    @property
    def final_grade(self):
        return float(self.__grade / self.__grade_count)

    def give_certificate(self):
        if self.final_grade >= self.__course.get_min_grade():
            self.__has_certificate = True
        else:
            self.__has_certificate = False

    def get_certificate(self):
        return self.__has_certificate

    def print_certificate(self):
        if self.__has_certificate:
            return f"certificate in the course: {self.__course.get_name()}"

    def unenroll(self, course):
        course.remove_enrollment(self)








