
with open("names.txt","at") as f:
    while True:
        name = input("Enter name [end to stop]:")
        if name == 'end':
            break
        f.write(name + "\n")


