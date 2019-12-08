def greet(*names, msg="Hello"):  # msg is keyword-only argument
    for n in names:
        print(msg, n)


greet("Bill", "Ben", "Elon", msg="Hi")
greet("Jason", "Billy")
