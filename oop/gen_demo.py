def unique(st):
    visited = []
    for c in st:
        if c not in visited:
            visited.append(c)
            yield c


def numbers():
    for i in range(1, 11):
        yield i


for c in unique("This is fine"):
    print(c)

g = numbers()
print(type(g))
print(next(g), next(g))

for v in numbers():
    print(v, end=' ')
