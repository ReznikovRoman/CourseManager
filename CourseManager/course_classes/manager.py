
from CourseManager.course_classes.person import Person
from CourseManager.course_classes.course import Course
from CourseManager.course_classes.student import Student
from CourseManager.course_classes.enroll import Enroll


class Manager(Person):
    courses_lst = []

    """
    Manager, who can create new Courses and edit them
    
    Args:
        first_n (str): Is used to determine a first name of a Manager
        last_n (str): Is used to determine a last name of a Manager
        phone (str): Is used to determine a phone number of a Manager
        date_of_birth (datetime.date): Is used to determine a date of birth of a Manager
        address (Address): Is used to determine an Address of a Manager
        salary (int): Is used to determine a salary of a Manager
        
    Attributes:
        __salary (int) : Stores salary
        __courses (int) : Stores Courses, which Manager can edit
        __permissions (str) : Stores Manager's permissions
    """

    def __init__(self, first_n, last_n, phone, date_of_birth, address, salary):
        super(Manager, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__salary = salary
        self.__courses = []
        self.__permissions = "manager"

    def add_course(self, course):
        """
        Manager can add Course to his 'List of Courses'

        Args:
            course (Course): Course, which will be added to the list

        Returns:

        """
        if course not in self.__courses:
            self.__courses.append(course)

    def create_course(self, course_name, course_id):
        """
        Creates a new Course

        Args:
            course_name (str): new Course's name
            course_id (str): new Course's ID

        Returns:
            new_course (Course): Created Course
        """
        new_course = Course(course_name, course_id, self.__permissions)
        if new_course not in Manager.courses_lst:
            Manager.courses_lst.append(new_course)
        return new_course

    def change_course_name(self, course: Course, new_name):
        """
        Changes a Course's name

        Args:
            course (Course): Course, which name will be changed
            new_name (str): new Course's name

        Returns:

        """
        if course in self.__courses:
            course.change_name(new_name, self.__permissions)

    def change_course_min_grade(self, course: Course, new_grade):
        """
        Manager can change the Course's min grade

        Args:
            course (Course): Course, which min grade will be changed
            new_grade (int): new Course's min grade

        Returns:

        """
        course.set_min_grade(new_grade, self.__permissions)

    def get_salary(self):
        """
        Returns:
            __salary
        """
        return self.__salary

    def get_manager_courses(self):
        """
        Returns:
            __courses
        """
        return self.__courses

    def get_permission(self):
        """
        Returns:
            __permissions
        """
        return self.__permissions

    def end_course(self, course):
        """
        Manager can finish the Course

        Args:
            course (Course): Course, which will be ended

        Returns:

        """
        if course.get_state() != "closed":
            course.change_state(new_state="closed", permissions=self.__permissions)

            enrolls = [enroll for enroll in course.get_enrollments()]
            for enroll in enrolls:
                enroll.give_certificate()
                enroll.get_student().unenroll(enroll)  # remove enroll from student
                course.remove_enrollment(enroll)  # remove enroll from the course

    def __len__(self):
        """

        Returns:
            Count of Courses, which manager can edit
        """
        return len(self.__courses)


