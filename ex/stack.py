
stack = []

while True:
    print("Menu")
    print("=====")
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    ch = int(input("Choice :"))
    if ch == 3:
        break

    if ch == 1:
        stack.append(input("Enter a name :"))
    elif ch == 2:
        if len(stack) > 0:
            print("Value poped : ", stack.pop())
        else:
            print("Stack is empty!")


