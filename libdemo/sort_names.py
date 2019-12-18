
names = []
with open("names.txt","rt") as f:
    for n in f:
        names.append(n.strip('\n'))

print(sorted(names))





