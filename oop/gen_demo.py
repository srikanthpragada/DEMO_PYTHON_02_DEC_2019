
def numbers():
    for i in range(1,11):
        yield i


g = numbers()
print(type(g))
print(next(g), next(g))

for v in numbers():
    print(v,end = ' ')