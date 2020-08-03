
from course_classes.person import Person


class Student(Person):
    """ Student, who is enrolled in a Course """
    def __init__(self, first_n, last_n, phone, date_of_birth, address):
        super(Student, self).__init__(first_n, last_n, phone, date_of_birth, address)
        self._enrolls = []

    def add_enroll(self, enroll):
        self._enrolls.append(enroll)

    def get_enrolls(self):
        return self._enrolls






