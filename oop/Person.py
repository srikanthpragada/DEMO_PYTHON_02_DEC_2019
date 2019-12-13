class Person:

    def __init__(self, name, age):
        self.name = name
        if age < 0 or age > 120:
            raise ValueError("Invalid Age!")

        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f"{self.name}-{self.age}"

    def __int__(self):
        return self.age

    @property
    def type(self):
        if self.age < 30:
            return "Young"
        elif self.age < 60:
            return "Middle Aged"
        else:
            return "Old"


p1 = Person("Abc", 130)
print(p1.type)

#
# p2 = Person("Xyz", 30)
# p3 = Person("Abc", 20)
#
# print(int(p1))
#
# print(p1 == p3)
# print(p2 > p1)
# print(str(p2))
# l = [1, 2, 3]
# print(l)  # str(l)  -> l.__str__()
