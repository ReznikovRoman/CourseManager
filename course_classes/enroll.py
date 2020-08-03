

class Enroll:
    """ Student's enrollment """
    def __init__(self, student, course):
        self._student = student
        self._course = course
        self._grade = None
        self._grade_count = 0

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
        return self._grade / self._grade_count








