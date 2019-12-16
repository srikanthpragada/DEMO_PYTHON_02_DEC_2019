class A:
    def process(self):
        print("A")


class B(A):
    pass


class C(B, A):
    def process(self):
        print("C")


obj = C()
obj.process()
