from course_classes.teacher import Teacher


class Course:
    """ Course, in which Students can enroll or which can be taught by a Teacher """
    def __init__(self, name, code, teacher=None):
        self._name = name
        self._code = code
        self._teachers = []
        self._enrollments = []

        if isinstance(teacher, Teacher):
            self._teachers.append(teacher)
        elif isinstance(teacher, list):
            self._teachers = teacher
        else:
            pass

    def get_name(self):
        return self._name

    def change_name(self, new_name):
        self._name = new_name

    def get_code(self):
        return self._code

    def get_teachers(self):
        return self._teachers

    def get_enrollments(self):
        return self._enrollments

    def add_teacher(self, teacher):
        self._teachers.append(teacher)

    def add_enrollment(self, enroll):
        self._enrollments.append(enroll)




