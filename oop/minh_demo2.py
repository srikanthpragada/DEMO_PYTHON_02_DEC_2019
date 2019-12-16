class A:
    def process(self):
        print("A")


class B(A):
    pass


class C:
    def process(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.process()
