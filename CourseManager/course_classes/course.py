from CourseManager.course_classes.teacher import Teacher


# TODO: Remove permissions arg (only managers have access to creating a new Course ==> no need in 'if statement')
#  OR add a decorator to all functions, where the permission check is needed
class Course:
    """
    Course, in which Students can enroll or which can be taught by a Teacher
    Course can be created only by a Manager

    Args:
        name (str): Is used to determine a name of the Course
        code (str): Is used to determine a code of the Course
        permissions (str): Is used to see who has created a new Course instance
        min_grade (int): Is used to determine a min grade, which Students need to have to be able to get a certificate
        teacher (str): Is used to determine teacher(s) in the Course
        state (str): Is used to determine whether the Course is open, closed or has another state

    Attributes:
        __name: Stores a name of the Course
        __code: Stores a code of the Course
        __teachers: Stores Course's teacher(s)
        __enrollments: Stores all Course's enrollments
        __min_grade: Stores a min grade of the Course
        __state: Stores a state of the Course
    """
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
                self.__teachers.extend(teacher)
            else:
                pass

    def get_name(self):
        """
        Returns:
            __name
        """
        return self.__name

    def change_name(self, new_name, permissions):
        """
        Changes name of the Course (only manager can change the name)

        Args:
            new_name (str): Course's new name
            permissions (str): Permissions of an invoker of this function

        Returns:

        """
        if permissions == "manager":
            self.__name = new_name

    def get_min_grade(self):
        """
        Returns:
            __min_grade
        """
        return self.__min_grade

    def set_min_grade(self, new_grade, permissions):
        """
        Updates min grade of the Course

        Args:
            new_grade (int): New min grade of the Course
            permissions (str): Permissions of an invoker of this function

        Returns:

        """
        if permissions == "manager":
            self.__min_grade = new_grade

    def get_code(self):
        """
        Returns:
            __code
        """
        return self.__code

    def get_teachers(self):
        """
        Returns:
            __teachers
        """
        return self.__teachers

    def get_enrollments(self):
        """
        Returns:
            __enrollments
        """
        return self.__enrollments

    def get_state(self):
        """
        Returns:
            __state
        """
        return self.__state

    def add_teacher(self, teacher):
        """
        Adds Teacher to the teachers list

        Args:
            teacher (Teacher): New Course's Teacher

        Returns:

        """
        self.__teachers.append(teacher)

    def add_enrollment(self, enroll):
        """
        Adds new enroll to the list of enrollments

        Args:
            enroll (Enroll): Enroll, which will be added to the enrollment list

        Returns:

        """
        self.__enrollments.append(enroll)

    def change_state(self, new_state, permissions):
        """
        Changes state of the Course

        Args:
            new_state (str):  New Course's State
            permissions (str): Permissions of an invoker of this function

        Returns:

        """
        if permissions == "manager":
            self.__state = new_state

    def remove_enrollment(self, enroll):
        """
        Removes enrollment from the enrollments list

        Args:
            enroll (Enroll): Enroll, which will be removed

        Returns:

        """
        self.__enrollments.remove(enroll)

    def __str__(self):
        """

        Returns:
            Course representation in a human-readable format
        """
        return f"Course Name: {self.__name};  Code: {self.__code}"




