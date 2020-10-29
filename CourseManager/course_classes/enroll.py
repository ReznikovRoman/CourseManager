from CourseManager.course_classes.course import Course


class Enroll:
    """
    Student's enrollment

    Args:
        student (Student): Is used to determine a Student, who wants to enroll in a Course
        course (Course): Is used to determine a Course, in which Student wants to enroll

    Attributes:
        __student (Student): Stores a student
        __course (Course): Stores a course
        __grades (list): Stores all Student's grades in the Course
        __has_certificate (bool): 'true' - if Student has a certificate in this Course, 'false' otherwise
    """
    def __init__(self, student, course: Course):
        self.__student = student
        self.__course = course
        self.__grades = []
        self.__has_certificate = False

    def get_student(self):
        """
        Returns:
            __student
        """
        return self.__student

    def get_course(self):
        """
        Returns:
            __course
        """
        return self.__course

    def get_grades(self):
        """
        Returns:
            __grades
        """
        return self.__grades

    def update_grade(self, new_grade):
        """
        Updates Student's final grade

        Args:
            new_grade (int): Student's new grade

        Returns:

        """
        self.__grades.append(new_grade)

    @property
    def final_grade(self):
        """
        Returns:
            Student's final (average) grade for the whole Course
        """
        try:
            return float(sum(self.__grades) / len(self.__grades))
        except ZeroDivisionError as e:
            print("Log: Students don't have marks")
            return 0
        except Exception as e:
            print("Log: Error {}".format(e))
            return -1

    def give_certificate(self):
        """
        If Student's (final grade > min_grade) - Adds Course's certificate to the Student

        Returns:

        """
        if self.final_grade >= self.__course.get_min_grade():
            self.__has_certificate = True
            new_certificate = f"Certificate in the course: {self.__course.get_name()}\n"
            self.__student.add_certificate(new_certificate)
        else:
            self.__has_certificate = False

    def get_certificate(self):
        """
        Returns:
            __has_certificate
        """
        return self.__has_certificate

    def unenroll(self, course):
        """

        Args:
            course (Course): Course, from which Student wants to unenroll

        Returns:

        """
        course.remove_enrollment(self)








