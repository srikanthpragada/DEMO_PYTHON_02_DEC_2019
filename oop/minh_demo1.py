class A:
    def process(self):
        print("A")


class B:
    def process(self):
        print("B")


class C(A, B):
    def calculate(self):
        print("C")


obj = C()
obj.process()
