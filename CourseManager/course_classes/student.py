from CourseManager.course_classes.person import Person


class Student(Person):
    """ Student, who is enrolled in a Course """
    def __init__(self, first_n, last_n, phone, date_of_birth, address, student_id):
        super(Student, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self.__enrolls = []
        self.__id = student_id
        self.__certificates = []

    def add_enroll(self, enroll):
        self.__enrolls.append(enroll)

    def get_enrolls(self):
        return self.__enrolls

    def get_id(self):
        return self.__id

    def unenroll(self, enroll):
        self.__enrolls.remove(enroll)

    def get_certificates(self):
        return self.__certificates

    def add_certificate(self, new_certificate):
        self.__certificates.append(new_certificate)

    def print_certificates(self):
        for i in range(len(self.__certificates)):
            print(f"{i+1} - {self.__certificates[i]}")






