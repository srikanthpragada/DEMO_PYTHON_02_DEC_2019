def process(func, a, b):
    return func(a, b)


def multiply(n1, n2):
    return n1 * n2


print(process(multiply, 10, 20))
print(process(lambda a,b : a + b, 10, 20))
