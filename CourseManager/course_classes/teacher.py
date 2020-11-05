from CourseManager.course_classes.person import Person


class Teacher(Person):
    """
    Teacher, who teaches Course(s) and can evaluate Students' assignments

    Args:
        first_n (str): Is used to determine a first name of a Teacher
        last_n (str): Is used to determine a last name of a Teacher
        phone (str): Is used to determine a phone number of a Teacher
        date_of_birth (datetime.date): Is used to determine a date of birth of a Teacher
        address (Address): Is used to determine an Address of a Teacher
        salary (int): Is used to determine a salary of a Teacher
        teacher_id (int): Is used to determine a teacher_id

    Attributes:
        __salary (int) : Stores all Teacher's saslary
        __courses (list) : Stores Courses, where Teacher is currently teaching
        __id (int) : Stores teacher_id
    """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary, teacher_id):
        super(Teacher, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__salary = salary
        self.__courses = []
        self.__id = teacher_id

    def get_salary(self):
        """
        Returns:
            __salary
        """
        return self.__salary

    def get_courses(self):
        """
        Returns:
            __courses
        """
        return self.__courses

    def add_course(self, course):
        """
        Adds course to the Teacher's list of Courses (now he will teach this course)

        Args:
            course (Course): Course, which will be added to the list

        Returns:

        """
        self.__courses.append(course)

    def get_id(self):
        """
        Returns:
            __id
        """
        return self.__id

    def set_grade(self, enroll, grade):
        """
        Updates grade for a given Enroll

        Args:
            enroll (Enroll): Enroll, which grade will be added
            grade (int): grade

        Returns:

        """
        enroll.update_grade(grade)

    def __len(self):
        """

        Returns:
            Count of Courses, which are taught by current Teacher
        """
        return len(self.__courses)

        
