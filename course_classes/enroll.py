
from course_classes.course import Course


class Enroll:
    """ Student's enrollment """
    def __init__(self, student, course: Course):
        self._student = student
        self._course = course
        self._grade = 0
        self._grade_count = 0
        self._has_certificate = False

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    def get_grade(self):
        return self._grade

    def get_grade_count(self):
        return self._grade_count

    def update_grade(self, new_grade):
        self._grade += new_grade
        self._grade_count += 1

    def get_final_grade(self):
        return float(self._grade / self._grade_count)

    def update_certificate(self, a_has_certificate):
        self._has_certificate = a_has_certificate

    def get_certificate(self):
        return self._has_certificate

    def print_certificate(self):
        if self._has_certificate:
            return f"certificate in the course: {self._course.get_name()}"








