def fun():
    print("Having fun!")


show = fun
print(id(fun), id(show))
fun()
show()


def fun(msg):
    print(msg)

print(id(fun))
# fun()  - points to old fun and no longer callable without parameter
show()
fun("Enjoy")
