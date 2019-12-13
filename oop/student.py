class Student:
    # Static attribute or class attribute
    courses = {'C': 5000, 'Python': 10000, 'Java': 15000}

    @classmethod
    def python_student(cls,admno,name):
        return cls(admno,name,"Python", Student.courses["Python"])

    @staticmethod
    def change_fee(course, newfee):
        Student.courses[course] = newfee

    # constructor

    def __init__(self, admno, name, course="C", feepaid=0):
        # object attributes
        self.admno = admno  # private attribute
        self.name = name
        self.course = course
        self.feepaid = feepaid

    # Methods
    def print(self):
        print("Admno   : ", self.admno)
        print("Name    : ", self.name)
        print("Course  : ", self.course)
        print("Feepaid : ", self.feepaid)

    def payment(self, amount):
        self.feepaid += amount

    def totalamount(self):
        return Student.courses[self.course]

    def getbalance(self):
        return self.totalamount() - self.feepaid


if __name__ == '__main__':

    # Student.change_fee("Python",12000) # call static method
    #
    # # Create objects
    # s1 = Student(1, "Andy", "Python", 5000)
    # s1.payment(2000)
    # s1.print()
    # print(s1.getbalance())

    p = Student.python_student(10,"Van")
    p.print()
