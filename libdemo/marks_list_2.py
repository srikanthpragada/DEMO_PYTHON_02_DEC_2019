
students = []

with open("marks.txt") as f:
    for line in f.readlines():
        parts = line.split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        total = sum(map(int,parts[1:]))

        avg = total / (len(parts) - 1)

        students.append( (name,total,avg))


for name,total,avg in sorted(students):
    print(f"{name:20} {total:5d} {avg:.2f}")


