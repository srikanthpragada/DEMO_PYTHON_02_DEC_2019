class InvalidCourseError(Exception):
    def __init__(self):
        self.message = "Invalid Course!"

    def __str__(self):
        return self.message


class Student:
    # Static attribute or class attribute
    courses = {'C': 5000, 'Python': 10000, 'Java': 15000}

    @classmethod
    def python_student(cls, admno, name):
        return cls(admno, name, "Python", Student.courses["Python"])

    @staticmethod
    def change_fee(course, newfee):
        Student.courses[course] = newfee

    # constructor

    def __init__(self, admno, name, course="C", feepaid=0):
        # object attributes
        self.admno = admno  # private attribute
        self.name = name
        if course not in Student.courses:
            raise InvalidCourseError()

        self.course = course
        self.feepaid = feepaid

    # Methods
    def print(self):
        print("Admno   : ", self.admno)
        print("Name    : ", self.name)
        print("Course  : ", self.course)
        print("Feepaid : ", self.feepaid)

    def payment(self, amount):
        tf = self.totalamount()
        if self.feepaid + amount > tf:
            raise ValueError("Feepaid is more than total fee!")
        else:
            self.feepaid += amount

    def totalamount(self):
        return Student.courses[self.course]

    def getbalance(self):
        return self.totalamount() - self.feepaid


if __name__ == '__main__':

    # Student.change_fee("Python",12000) # call static method
    #
    # # Create objects
    try:
        s1 = Student(1, "Andy", "C#", 5000)
    except InvalidCourseError as ex:
        print(ex)

    # s1.payment(2000)
    # s1.print()
    # print(s1.getbalance())
