from CourseManager.course_classes.person import Person


class Student(Person):
    """
    Student, who can be enrolled in a Course

    Args:
        first_n (str): Is used to determine a first name of a Student
        last_n (str): Is used to determine a last name of a Student
        phone (str): Is used to determine a phone number of a Student
        date_of_birth (datetime.date): Is used to determine a date of birth of a Student
        address (Address): Is used to determine an Address of a Student
        student_id (int): Is used to determine a student_id of a Student

    Attributes:
        __enrolls (list) : Stores all Student's enrollments
        __id (int) : Stores Student's id
        __certificates (list) : Stores Student's certificates
    """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, student_id):
        super(Student, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__enrolls = []
        self.__id = student_id
        self.__certificates = []

    def add_enroll(self, enroll):
        """
        Adds new enroll to the Student's list of enrollments

        Args:
            enroll (Enroll): enroll, which will be added to the list

        Returns:

        """
        self.__enrolls.append(enroll)

    def get_enrolls(self):
        """
        Returns:
            __enrolls
        """
        return self.__enrolls

    def get_id(self):
        """
        Returns:
            __id
        """
        return self.__id

    def unenroll(self, enroll):
        """
        Removes student enrollment to the Course

        Args:
            enroll (Enroll): enroll, which will be removed

        Returns:

        """
        self.__enrolls.remove(enroll)

    def get_certificates(self):
        """
        Returns:
            __certificates
        """
        return self.__certificates

    def add_certificate(self, new_certificate):
        """
        Adds certificate to the certificates list

        Args:
            new_certificate (str): certificate, which will be added to the list

        Returns:

        """
        self.__certificates.append(new_certificate)

    def print_certificates(self):
        """
        Prints all Student's certificates (if any)

        Returns:

        """
        for i in range(len(self.__certificates)):
            print(f"{i+1} - {self.__certificates[i]}")






