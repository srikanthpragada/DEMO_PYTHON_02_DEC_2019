g = 1000  # Global


def fun1():
    counter = 0  # Enclosing variable
    global g
    g = 2000

    def fun2():
        nonlocal counter
        b = 200  # Local variable
        counter = counter + 1
        print(g, b)

    fun2()
    fun2()
    print(counter)


fun1()
print(g)
