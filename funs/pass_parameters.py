def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend_zero(lst):
    lst.insert(0, 0)


a = 100
l = [1, 2]
print(id(a))
zero(a)
print(a)

prepend_zero(l)
print(l)
