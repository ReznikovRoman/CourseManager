from CourseManager.course_classes.teacher import Teacher


class Course:
    """ Course, in which Students can enroll or which can be taught by a Teacher """
    def __init__(self, name, code, permissions, min_grade=4, teacher=None, state="open"):
        if permissions == "manager":
            self.__name = name
            self.__code = code
            self.__teachers = []
            self.__enrollments = []
            self.__min_grade = min_grade
            self.__state = state

            if isinstance(teacher, Teacher):
                self.__teachers.append(teacher)
            elif isinstance(teacher, list):
                self.__teachers = teacher
            else:
                pass

    def get_name(self):
        return self.__name

    def change_name(self, new_name, permissions):
        if permissions == "manager":
            self.__name = new_name

    def get_min_grade(self):
        return self.__min_grade

    def set_min_grade(self, new_grade, permissions):
        if permissions == "manager":
            self.__min_grade = new_grade

    def get_code(self):
        return self.__code

    def get_teachers(self):
        return self.__teachers

    def get_enrollments(self):
        return self.__enrollments

    def get_state(self):
        return self.__state

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def add_enrollment(self, enroll):
        self.__enrollments.append(enroll)

    def change_state(self, new_state, permissions):
        if permissions == "manager":
            self.__state = new_state

    def remove_enrollment(self, enroll):
        self.__enrollments.remove(enroll)

    def __str__(self):
        return f"Course Name: {self.__name};  Code: {self.__code}"




